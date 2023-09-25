import utils, read_csv, charts

def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Type your country: ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_char(country['Country'], labels, values)
    charts.generate_pie_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()