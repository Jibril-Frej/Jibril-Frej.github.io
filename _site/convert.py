import re


# Function to convert a single LaTeX \item to Markdown format
def convert_latex_to_markdown(latex_item):
    # Extract title, publication, authors, and link using regex patterns
    title_pub_pattern = r"\\item\s*(.*),\s*\\textcolor\{.*?\}\{(.*?)\}"
    authors_pattern = r"\\underline\{(.*?)\},\s*(.*?)\\"
    link_pattern = r"\\url\{(.*?)\}"

    title_pub_match = re.search(title_pub_pattern, latex_item)
    authors_match = re.search(authors_pattern, latex_item)
    link_match = re.search(link_pattern, latex_item)

    if title_pub_match and authors_match and link_match:
        title = title_pub_match.group(1)
        publication = title_pub_match.group(2)
        main_author = authors_match.group(1)
        co_authors = authors_match.group(2)
        link = link_match.group(1)

        # Format into Markdown
        markdown = f"- **{title}**, *{publication}*\n  <u>{main_author}</u>, {co_authors}\n  [{link}]({link})"
        return markdown
    else:
        return "Error: Could not parse LaTeX string."


# Example LaTeX string
latex_item = r"\item Course Recommender Systems Need to Consider the Job Market, \textcolor{maincol}{SIGIR 2024}\\ \underline{J Frej}, A Dai, S Montariol, A Bosselut, T Käser\\\url{https://arxiv.org/pdf/2404.10876}"

# Convert the example LaTeX item
converted_markdown = convert_latex_to_markdown(latex_item)
converted_markdown
