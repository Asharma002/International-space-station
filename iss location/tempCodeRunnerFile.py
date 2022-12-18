df2 = px.data.gapminder().query("year == 2007")
# fig1 = px.scatter_geo(df2, locations="iso_alpha",
#                      color="continent", # which column to use to set the color of markers
#                      hover_name="country", # column added to hover information
#                      size="pop", # size of markers
#                      projection="natural earth")
# fig1.show()
