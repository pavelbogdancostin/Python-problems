from prettytable import PrettyTable

def credit_rata_fixa(valoare,rata_dobanzii=6,numar_rate=120):
	""" docstring """
	dobanda_lunara=rata_dobanzii/12/100
	indice=1+dobanda_lunara
	putere=indice ** numar_rate
	plata_constanta=valoare * dobanda_lunara/(1-1/putere)
	luna = 1
	sold_datorat = valoare
	total_plati_principal = 0
	total_dobanzi = 0
	afiseaza = PrettyTable()
	afiseaza.field_names=['luna','sold_inceputul_lunii','dobanda_lunara',
							'principal_lunar','rata','sold_sfarsit']
	while sold_datorat > 0:
		dobanda_luna = sold_datorat*dobanda_lunara
		principal_luna = plata_constanta-dobanda_luna
		sold_sfarsitul_lunii = sold_datorat - principal_luna
		total_plati_principal += principal_luna
		total_dobanzi+=dobanda_luna
		afiseaza.add_row([ luna, round(sold_datorat,2), round(dobanda_luna,2),
						   round(principal_luna,2),round(plata_constanta,2),
						   round(sold_sfarsitul_lunii,2)])


		afiseaza.add_row(['-' * 12, '-' * 23, '-' * 16, '-' * 17,'-' * 12,'-' * 14])
		luna += 1
		sold_datorat -= principal_luna


	#afiseaza.add_row(['Total', '---', '{:.2f}'.format(total_plati_principal), '', '', '{:.2f}'.format(total_dobanzi)])


	afiseaza.add_row(['Total', '---', round(total_plati_principal,2), '', '', round(total_dobanzi,2)])

	print(afiseaza)
	print('Total plati', round(total_plati_principal,2))
	print('Total dobanzi', round(total_dobanzi,2))

credit_rata_fixa(10000)