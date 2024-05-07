from bs4 import BeautifulSoup
import os
import codecs
import io

# Directory contenente i file .md
directory = 'blog'

# Percorre tutti i file nella directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        with codecs.open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')

            # Trova tutti i div con classe 'wp-block-image'
            wp_block_images = soup.find_all('div', class_='wp-block-image')

            # Per ogni div trovato, trova il tag img e recupera il valore dell'attributo src
            for wp_block_image in wp_block_images:
                img_tag = wp_block_image.find('img')
                if img_tag:
                    src = img_tag.get('src')
                    print("SRC trovato:", src)

                    # Sostituisci l'intero blocco con il tuo codice desiderato
                    replacement = '{{< image src="/img/uploads/' + src + '" >}}'
                    wp_block_image.replace_with(replacement)

        # Scrivi il contenuto modificato nel file
        with io.open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
            file.write(unicode(soup))
