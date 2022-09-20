Following are the steps to execute the code:

Kindly, install the requirements.txt file from repository link to get all the dependecies in local.

    Repository link-https://github.com/pasta29/assignment

1-Go to directory of "news.py" (GitHub path- https://github.com/pasta29/assignment/tree/main/new_scraper/new_scraper/spiders) and execute following crawler argument:
	
	
	argument/command - scrapy crawl -s MONGODB_URI="mongodb+srv://pasta:pasta_qwerty@pythoncluster.zqoyn8m.mongodb.net/?retryWrites=true&w=majority" -s MONGODB_DATABASE="NewsDatabase" news
	
	argument specification=> python cluster's username-pasta
							 	            password- pasta_qwerty
											databse_name-NewsDatabase
											


	Note-Once above comand is succesfull then the news data will be pulled and stored in MongoDB database.


2-To run the API execute the file "searchApi.py" in command prompt using command "python searchApi.py" :
	GitHub Link for the file-https://github.com/pasta29/assignment/blob/main/searchAPI/searchApi.py
	
	once API is executed succesfully, run the below link in browser locally to fetch the results.
	
	browser/local host link- localhost:3001/search?search=russia
	
	Note- search keyword is "russia" in local host link, it will hit the MongoDB collection and fetch all the news articles having keyword "russia", keyword can be changed and searced accordingly.
	
	
3-Below is main reository link where all the python files and dependencies are present.

	Repository link-https://github.com/pasta29/assignment
	

	