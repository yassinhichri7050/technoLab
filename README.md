sequential_crawl.py Ce script implémente un processus de crawling séquentiel en utilisant une session partagée, ce qui permet de conserver les données de session entre plusieurs requêtes. Voici les étapes principales exécutées dans ce script :

Récupération des URLs à crawler depuis un fichier Sitemap XML.

Démarrage d'un navigateur configuré pour fonctionner en mode "headless" (sans interface graphique), afin de maximiser les performances.

Exploration des URLs une par une :

Génération de fichiers Markdown pour documenter le contenu de chaque URL.

Gestion des erreurs pour identifier les éventuelles URLs ayant échoué lors du crawl.

Fermeture propre du navigateur après l'exécution.

À utiliser si vous souhaitez un contrôle minutieux des séquences d'exploration ou si vos besoins nécessitent une session partagée.

    parallel_craw.py Ce script effectue un crawling parallèle pour maximiser la vitesse en explorant plusieurs URLs simultanément. Voici ce que fait ce script :

Récupération des URLs à crawler depuis un fichier Sitemap XML.

Démarrage d'un navigateur configuré pour fonctionner en mode "headless", offrant les mêmes optimisations que dans le script séquentiel.

Lancement de tâches asynchrones en parallèle :

Exploration de plusieurs URLs simultanément pour améliorer les performances.

Génération de fichiers Markdown pour documenter le contenu de chaque URL.

Gestion indépendante des erreurs pour chaque tâche.

Le navigateur est automatiquement fermé à la fin de l'exécution grâce au mot-clé async with.

Approprié pour les projets nécessitant un traitement rapide d'un grand nombre d'URLs.

    single_craw.py Ce script est une implémentation simple et minimale pour effectuer un crawling sur une unique URL. Voici ses principales caractéristiques :

Utilisation de l'objet AsyncWebCrawler pour explorer une seule page web.

Récupération du contenu de la page et conversion en Markdown.

Affichage du contenu Markdown dans la console pour un usage rapide.

Ce script est idéal pour tester l’outil crawl4ai sur une URL donnée ou pour des besoins ponctuels.
