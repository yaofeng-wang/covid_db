from scraper import get_soup_from_url, extract_data_from_post, get_post_url, MOH_COVID_URL 
from utils import save

def main():
    # Get URL of the post containing latest daily COVID-19 data from MOH website.
    soup = get_soup_from_url(MOH_COVID_URL)
    post_url = get_post_url(soup)

    # Extract data from post.
    soup = get_soup_from_url(post_url)
    data = extract_data_from_post(soup)

    # Save data into database.
    save(data)

if __name__ == "__main__":
    main()