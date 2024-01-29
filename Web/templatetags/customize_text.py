from django import template

register = template.Library()

@register.filter(name='split')
def split(text):
  return text.split("\n")

@register.filter(name='currency_symbol')
def currency_symbol(country_code='ae'):
  symbol = ''

  if country_code == 'ae':
    symbol = 'AED'
  elif country_code == 'in':
    symbol = '₹'

  return symbol
