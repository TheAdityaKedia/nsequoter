# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 12:08:27 2016

@author: adi
"""
import requests
import sys
import re
import datetime
import calendar

#utility class implementing the helper funtions for nsequoter
#all functions are weakly private
class Utils():
    
    _base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
    _FO_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying="
    _months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    _now = datetime.date.today()
    _month = _now.month
    _year = _now.year
    _date = _now.day
    _weekday = _now.isoweekday()
    _codes = {} #constructor will build this with stocks currently traded on the nse

    #cunstructor
    def __init__(self):
        self._build_codes_dict()
        
    #getting the requested page to be scraped and raising exceptions when valid
    def _get_page_or_exception(self, url):
        
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            print (e)
            sys.exit(1)
        except requests.exceptions.Timeout as e:
            print (e)
            sys.exit(1) 
        except requests.exceptions.RequestException as e:
            print (e)
            sys.exit(1)
        if r.status_code != 200:
            r.raise_for_status()
        return r
    
    #for equity derivatives    
    def _get_last_thursday(self, y, mon): 
        
        days = calendar.monthrange(y, mon)
        dt= datetime.date(y, mon, days[1])
        offset = 4 - dt.isoweekday()
        if offset > 0: offset -= 7
        dt += datetime.timedelta(offset)
        return dt.day
        
    #for currency derivatives (to be implemented in the next version)    
    def _get_last_wednesday(self, y, mon): 
        
        days = calendar.monthrange(y, mon)
        dt= datetime.date(y, mon, days[1])
        offset = 3 - dt.isoweekday()
        if offset > 0: offset -= 7
        dt += datetime.timedelta(offset)
        return dt.day
    
    #builds the dictionary of curently traded stock codes
    def _build_codes_dict(self):
        url = 'https://www.nseindia.com/content/equities/EQUITY_L.csv'
        r=self._get_page_or_exception(url)
        items = r.text.splitlines()
        for i in range(len(items)):
            items[i]=items[i].split(',')
        for i in range(len(items)):
            self._codes[items[i][0]]=items[i][1]
    
    
    def get_quote(self, eq: str, cont: Optional[str] = 'EQ', mon: Optional[Union[str, int]] = _month) -> float:
        """
        Given a ticker for a security and optinally a month of the year, this funciton gets the price
        for the underlying security or the futures contract for the given month as a 3 letter string or
        an integer value.
        
        Args:
        
        Return:
        
        """
        
        eq = eq.upper()        
        if eq not in self._codes:
            raise Exception('Invalid Symbol/Code!')
        
        if cont == 'EQ':
            url = self._base_url+eq.upper()
            
        elif cont == 'FUTSTK':
            if type(mon) == int:
                mon == self._months[mon - 1]
            else:
                mon = mon.upper() 
            if ((self._months.index(mon)+1) > ((self._month+2)%12)) or ((self._months.index(mon)+1) < self._month):
                raise Exception('Contract not available!')
            y = self._year

            if isinstance(mon, int):
                datetime_obj = datetime.strptime(mon, %m)
                mon = datetime_obj.strftime(%b)

            if (self._month == 'DEC') and (mon == 'JAN' or 'FEB'): y+=1
            d = self._get_last_thursday(y, (self._months.index(mon)+1))
            if self._date > d:
                raise Exception('Contract Expired!')
            url = self._FO_url+eq+'&instrument=FUTSTK&expiry='+str(d)+mon+str(y)
        else:
            raise Exception('Facility not available yet!') 
            
        pattern = r'"lastPrice":"(\d*,?\d*\.\d*)"'  
        r=self._get_page_or_exception(url)
        match = re.findall(pattern, r.text)
        quote = match[0].replace(',','')
        return float(quote)
