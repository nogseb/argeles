# Argelès, Nouvel An 2027 — carnet de voyage

Carnet de voyage interactif du séjour à Argelès-sur-Mer pour la Saint-Sylvestre (29 décembre 2026 – début janvier 2027), à cinq : maison HomeExchange, programme jour par jour, Réveillons de la Plage, escapades, carte schématique, météo, préparatifs.

Publié sur **https://nogues.app/argeles/**.

## Organisation

| Élément | Rôle |
|---|---|
| `src/page.html` | Source du site (également publiée en artifact Claude) |
| `build.py` | Construit `docs/index.html` à partir de la source |
| `docs/index.html` | Le site complet, en un seul fichier |
| `docs/.htaccess` | Exclut le carnet des moteurs de recherche |
| `.github/workflows/deploy-ovh.yml` | Publie `docs/` sur l'hébergement OVHcloud à chaque mise à jour |

Le contenu du séjour est regroupé au début du script, dans les constantes `PLACES`, `DAYS`, `FEST`, `TRIPS`, `PACK` et `RESA`.

## Publication

Chaque modification poussée sur `main` dans `docs/` publie le site vers `www/argeles` sur l'hébergement OVHcloud de nogues.app. Le workflow attend les secrets `OVH_SFTP_HOST`, `OVH_SFTP_USER` et `OVH_SFTP_PASSWORD`, identiques à ceux des autres sites de nogues.app.
