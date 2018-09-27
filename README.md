# RecommenderEngine

Create product recommendation engine for users

## Run scoring function:
`python command.py initialize --users-file <path user file> --products-file <path product file> --current-timestamp <timestamp>`

Example:
`python command.py initialize -u input/users.txt -p input/product_score.txt -ct 1509833366`

## Recommend product based on UID:
`python command.py recommend-products --user-id <USER ID>`

Example:
`python command.py recommend-products --user-id 12342`

## Structure:
```
.
├── command.py
├── main.py
├── input
│   ├── product_score.txt
│   └── users.txt
└── output
    ├── new_recommendation.txt
    └── new_users_preference.txt
```