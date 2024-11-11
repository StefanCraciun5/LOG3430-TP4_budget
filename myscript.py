import os

badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"  # commit problématique
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # dernier commit stable

# Démarrer git bisect avec les commits connus
os.system(f"git bisect start {badhash} {goodhash}")

# Exécuter git bisect avec la commande de test
os.system("git bisect run python manage.py test")