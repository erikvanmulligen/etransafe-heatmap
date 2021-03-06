import json
from knowledgehub.api import KnowledgeHubAPI
import argparse


def test():
	parser = argparse.ArgumentParser(description='test similarity service')
	parser.add_argument('-username', required=True, help='username')
	parser.add_argument('-password', required=True, help='password')
	args = parser.parse_args()

	api = KnowledgeHubAPI()
	api.set_service('DEV')
	status = api.login(args.username, args.password)
	print(status)
	terms = api.SemanticService().lookup('Terbinafine', 'RxNorm')
	print(json.dumps(terms, indent=4, sort_keys=True))
	#if len(terms['terms']) > 0:
		#concepts = api.SemanticService().normalize(terms['terms'][0], 'RxNorm')
		#print(json.dumps(concepts, indent=4, sort_keys=True))

		#if len(concepts['concepts']) == 1:
	compounds = [
							  "Minoxidil","Estradiol","Anastrozole","Felodipine","Amphetamine",",Adenosine","Azathioprine","Levamisole",
							  #"Zolmitriptan","Lidocaine","Alprazolam","Ropivacaine","Foscarnet","Rimonabant","Remoxipride","Cyclophosphamide",
							  #"Aripiprazole","Bambuterol","Sulfamethoxazole","Rosiglitazone","Clozapine","Budesonide","Omeprazole","Raltitrexed",
							  #"Clonidine","Gefitinib","Ximelagatran","Diazepam","Olanzapine","Zafirlukast","Nifedipine","Indomethacin","Erlotinib",
							  #"Formoterol","Diclofenac","Metoprolol","Enprofylline","Bicalutamide","Chlordiazepoxide","Simvastatin","Ranitidine",
							  #"Ticagrelor","Sulfinpyrazone","Phenylbutazone","Benazepril","Isosorbide Mononitrate","Deferoxamine","Guanfacine",
							  #"Naftifine","Chlorthalidone","Guanethidine","Valproic Acid","Clozapine","Baclofen","Maprotiline","Thioridazine",
							  #"Aminoglutethimide","Bromocriptine","Phentolamine","Amantadine","Thiethylperazine","Pindolol","Lidocaine",
							  #"Linezolid","Prednisolone","Candoxatril","Diazepam","Orlistat","Carprofen","Cilazapril"
							  ]

	# studies = api.Medline().getStudiesByCompoundNames(compounds) + \
					 #api.Faers().getStudiesByCompoundNames(compounds) + \
					 #api.ClinicalTrials().getStudiesByCompoundNames(compounds) + \

	# studies = api.eToxSys().getStudiesByCompoundNames(compounds)
	# print(json.dumps(studies, indent=4, sort_keys=True))
	# print(len(studies))


if __name__ == "__main__":
    test()