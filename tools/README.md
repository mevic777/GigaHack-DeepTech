# GigaHack-BioTech - Docky

## Inspiration
For our team, it is a pleasure to see the world of computer technology and AI help and contribute to efforts in solving real world medical problems and struggles. This is why we wanted to make a tool that helps valuable scientists and researchers achieve their goal in the betterment of the field. Enter Docky - the Biomedical Research AI Agent.

## What it does
Docky uses the Wisecube API for extracting detailed medical data from revised research articles from the whole web and the technologies of OpenAI to contextualize the data and make it relevant for the researcher, which is served to the user in a convenient web interface.

## How we built it
Our simple and elegant web application was created using pure HTML, CSS and JavaScript. All assets from both the landing page and the chatroom were all custom made by our team to ensure the best quality of the product.

The frontend connects with our custom backend, composed from specialised scripts and tools powered by Python3 and the APIs of Wisecube and OpenAI. When a question is inquired, the prompt goes to Wisecube to extract all relevant information, which is then piped into our custom OpenAI model to formulate a proper (or better) answer. Our model was fine-tuned with a large, specific dataset, instructed to compose accurate, verbose answers, while also citing its sources.

## Challenges we ran into
As our team strives for perfection, the user experience was a challenging aspect of our work. Great effort has been made in combining a sleek, clean design with a user-friendly interface.

Due to the fact that the `openai` python API has less-than-desirable web support, compatibility between the frontend and backend was also a tough challenge, which has been overcome by our talented engineers.

Since we acknowledge the potential of our product, creating everything in the spirit of maintainability and expandability was among one of our concerns as well.

## Accomplishments that we're proud of
Our team prides itself in creating a functional prototype in less than 2 days of hard, assiduous work, while also maintaining a good relationship with each other, our mentors and our trackers.

We are proud of creating a product which uses the power of two(!) AI frameworks to create good, high-quality results.

## What we learned
Each member of our team has made great efforts in materializing our idea and we can confidently say that our skills in web development, python and working with large language models have all increased significantly.

We also learned the importance of APIs and how to efficiently make use of them

Last but not least, we reinforced our workplace relationships and strengthened our bonds, learning how to come together and better cooperate.

## What's next for 1D3M-BioTech
Our product has a lot of potential, especially in academia, public and private health institutions. We plan on developing our product further on the technical side and create a business plan, while also looking into the legal side of things.

-----------------------------------------

## Personality & API keys
The finetuning management tools require an OpenAI API key and a personality prompt, which are put in txt files in plaintext.
