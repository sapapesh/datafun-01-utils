''' This module provides a reusable byline for the author's services. '''

import math
import statistics

    #variable list
company_name: str = "Analytics is Fun, Inc"
company_description: str = "Learning analytics while playing with numbers"
company_founding_year: int = 2024
company_city: str = "Tulsa"
company_state: str = "Oklahoma where the wind comes sweeping down the plains"
company_number_employees = 4
company_offers_benefits: bool = True
services_offered: list = ["Learning Python", "Natural Language Processing", "Data Mining", "Display Best Practices"]
service_price: list = [400, 200, 100, 500]
has_international_presence: bool = False
average_service_price: float = 150

company_offers_benefits_string: str = f"Offers Benefits: {company_offers_benefits}"
international_presence_string: str = f"International Presence: {has_international_presence}"
average_service_price_string: str = f"Average Service Price: {average_service_price}"

smallest= min(service_price)
largest= max(service_price)
total= sum(service_price)
count= len(service_price)
mean= statistics.mean(service_price)
mode= statistics.mode(service_price)
median= statistics.median(service_price)
standard_deviation=statistics.stdev(service_price)

stats_string: str = f"""
    Descriptive Statistics for Our Service Prices:
      Smallest: {smallest}
      Largest: {largest}
      Total: {total}
      Count: {count}
      Mean: {mean}
      Mode: {mode}
      Median: {median}
      Standard Deviation: {standard_deviation}
"""
    
byline: str = f"""
    {company_name}
    {company_description}
    {company_founding_year}
    {international_presence_string}
    {company_offers_benefits_string}
    {average_service_price_string}
    {stats_string}
"""

def main():
    ''' Display all output'''
print(company_name)
print(company_description)
print(company_founding_year)
print(international_presence_string)
print(company_offers_benefits_string)
print(average_service_price_string)
print(stats_string)

print(byline)
