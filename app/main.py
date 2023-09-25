import utils, read_csv, charts, pandas as pd

def run():
  df = pd.read_csv('./data.csv') 
  df = df[df['Continent'] == 'Africa']
  countries = df['Country'].values
  percentage = df['World Population Percentage'].values
  charts.generate_bar_char('Africa', countries, percentage)
  charts.generate_pie_chart('Africa', countries, percentage)

#   if len(result) > 0:
#     country = result[0]
#     labels, values = utils.get_population(country)
#     charts.generate_bar_char(country['Country'], labels, values)
#     charts.generate_pie_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()