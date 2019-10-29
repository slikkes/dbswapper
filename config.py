file = ".env"

databases = dict(
	prod = dict(
		DB_CONNECTION="mysql",
		DB_HOST="10.0.2.1",
		DB_PORT="3306",
		DB_DATABASE="prod",
		DB_USERNAME="produser",
		DB_PASSWORD="yxcvawr"
		),
	dev = dict(
		DB_CONNECTION="localhost",
		DB_HOST="127.0.0.1",
		DB_PORT="3306",
		DB_DATABASE="homestead",
		DB_USERNAME="root",
		DB_PASSWORD="vagrant"
		)
	)