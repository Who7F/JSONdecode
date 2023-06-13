import urllib.request
import json

def main():
    # Define the URL to fetch country data
    url = 'https://restcountries.com/v3.1/name/'
    
    # Specify the country name to retrieve information for
    name = 'deutschland'
    
    # Open a request to the specified URL
    request = urllib.request.urlopen(url + name)
    
    # Read the JSON response from the request
    jsonfile = request.read()
    
    # Close the request after reading
    request.close()
    
    # Parse the JSON data into a Python dictionary
    file = json.loads(jsonfile)
    
    # Print the official name of the country in German
    print(file[0]['name']['nativeName']['deu']['official'])
    

if __name__=='__main__':
    # Execute the main function
    main()
