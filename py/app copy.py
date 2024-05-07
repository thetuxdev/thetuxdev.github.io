import os
import re

# Cartella contenente i file .md
folder_path = "blog"

# Espressione regolare per individuare il blocco HTML da sostituire
pattern = r'<div class="wp-block-image">\s*<figure class="aligncenter size-full"><img decoding="async" src="(.*?)" alt="" class="wp-image-\d+" />\s*</figure>\s*</div>'

# Loop attraverso i file nella cartella
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        file_path = os.path.join(folder_path, filename)

        # Leggi il contenuto del file
        with open(file_path, 'r') as file:
            content = file.read()

        # Individua il blocco HTML da sostituire
        match = re.search(pattern, content)
        if match:
            img_src = match.group(1)

            # Costruisci il nuovo blocco HTML con l'URL dell'immagine
            new_content = re.sub(pattern, '{{< image src="/img/uploads/' + os.path.basename(img_src) + '" >}}', content)

            # Sovrascrivi il file con il nuovo contenuto
            with open(file_path, 'w') as file:
                file.write(new_content)
