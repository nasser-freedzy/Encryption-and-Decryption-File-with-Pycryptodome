##############################################################################################################################################
# Chiffrement et Déchiffrement de Fichiers avec AES

Ce script Python permet de chiffrer et déchiffrer des fichiers en utilisant l'algorithme de chiffrement AES (Advanced Encryption Standard). Il utilise le module `pycryptodome` pour le chiffrement et le déchiffrement, et le module `hashlib` pour générer une clé de chiffrement à partir d'un mot de passe.

## Fonctionnalités

- **Chiffrement** : Chiffre un fichier donné à l'aide d'un mot de passe.
- **Déchiffrement** : Déchiffre un fichier chiffré en utilisant le même mot de passe.
- **Performance** : Mesure le temps nécessaire pour exécuter les opérations de chiffrement et déchiffrement.

## Prérequis

- Python 3.x
- Bibliothèque `pycryptodome`

Vous pouvez installer `pycryptodome` avec pip :

```bash
pip install pycryptodome
```

## Utilisation

Le script s'exécute à partir de la ligne de commande avec la syntaxe suivante :

```bash
python script.py <mode> <password> <filename>
```

### Arguments

- `<mode>` : Mode d'opération, soit `-e` pour chiffrer, soit `-d` pour déchiffrer.
- `<password>` : Mot de passe utilisé pour générer la clé de chiffrement.
- `<filename>` : Nom du fichier à chiffrer ou déchiffrer.

### Exemples

Pour chiffrer un fichier :

```bash
python script.py -e monMotDePasse fichier.txt
```

Pour déchiffrer un fichier :

```bash
python script.py -d monMotDePasse fichier.txt
```

## Fonctionnement du Code

1. **Chiffrement** (`encryptFile`):
   - Génère une clé de chiffrement à partir du mot de passe avec SHA-256.
   - Ouvre le fichier et le lit en mode binaire.
   - Rembourre les données pour les rendre multiples de 16 octets.
   - Chiffre les données avec AES en mode CBC et écrit le résultat dans le même fichier.

2. **Déchiffrement** (`decrytFile`):
   - Génère la même clé de chiffrement à partir du mot de passe.
   - Lit le fichier chiffré.
   - Déchiffre les données et enlève le rembourrage avant de réécrire le fichier.

## Remarques

- Assurez-vous que le mot de passe utilisé pour le chiffrement est le même que celui utilisé pour le déchiffrement.
- Le vecteur d'initialisation (IV) est codé en dur dans le script. Pour une meilleure sécurité, envisagez d'utiliser un IV aléatoire et de le stocker avec le fichier chiffré.

## Avertissements

L'utilisation de cryptographie nécessite une bonne compréhension des principes de sécurité. Veuillez en tenir compte lors de l'utilisation de ce script.
```

Ce `README.md` décrit le code, ses fonctionnalités, son utilisation, et donne des conseils pour la sécurité.
