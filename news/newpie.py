import click
import requests

# the apikey you got from newsapi.org
API_KEY = 'f45fa2c71932483f832f0cc745af0325'

@click.group()
def main():
        """
        NEW PIE-version 1 is a news app that gives you a list of 4 sources from which you choose one,
        Then from your choice it returns a list of the top 10 headlines,
        The news headline has a title, description and a url in case the user needs to follow up
        The user also needs to have a valid news api created from http://www.newsapi.org
        """
        pass

@main.command()

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=f45fa2c71932483f832f0cc745af0325"

	# fetching data in json format 
	open_source = requests.get(main_url).json() 

	# getting all articles in a string sources
	source = open_source["sources"] 

	# empty list which will 
	# contain all trending newssources 
	results = [] 
	
	for s in source: 
                results.append(s["id"])
            
   	
	for i in results[0:4]:
            print(i)	


@main.command()
def topheadlines():
          """ Please enter your choice from the listsources """
          newsSource = click.prompt("Please enter your choice from listsources")
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=f45fa2c71932483f832f0cc745af0325&sources="+newsSource

	# fetching data in json format 
          open_headline = requests.get(main_url).json() 

	# getting all headlines in a string articles 
          headline = open_headline["articles"] 

	# empty list which will 
	# contain all trending newssources 
          output = [] 
	
          for h in headline: 
                click.echo('\n')
                click.secho(click.style('TITLE: ' + h['title'], fg='green'))
                click.secho(click.wrap_text(h['description']))
                click.secho(click.style('DOMAIN: ' + h['url'], fg='blue'))
           
           	
          for i in output[:11]:
                print(i)


if __name__ == '__main__':
	main()
