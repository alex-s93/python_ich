// 1. Из коллекции sample_airbnb.listingsAndReviews найдите среднюю цену за сутки проживания на Гавайских островах.
db.airbnb.aggregate([
    {
        $match: {
            "address.location.coordinates": {
                $geoWithin: {
                    $geometry: {
                        type: "Polygon",
                        coordinates: [
                            [
                                [
                                    -160.45201401478644,
                                    21.785338793790658
                                ],
                                [
                                    -155.6552788846446,
                                    18.87841223834408
                                ],
                                [
                                    -154.57738808184902,
                                    19.515895418757754
                                ],
                                [
                                    -155.9218739512767,
                                    20.83996547342511
                                ],
                                [
                                    -159.3793127398141,
                                    22.48017496178465
                                ],
                                [
                                    -160.45201401478644,
                                    21.785338793790658
                                ]
                            ]
                        ]
                    }
                }
            }
        }
    },
    {
        $group:
            {
                _id: null,
                avg_price: {
                    $avg: "$price"
                }
            }
    },
    {
        $project:
            {
                avg_price: 1,
                _id: 0
            }
    }
])
// Ответ: 231.4853420195439739413680781758958


// 2. 2.Подсчитайте в коллекции sample_mflix.movies, сколько фильмов имеют imdb рейтинг выше 8 и выходили в период
// с 2015 до 2023 года (используем year)
db.movies.aggregate([
    {
        $project:
            {
                released_year: {
                    $year: "$released"
                },
                "imdb.rating": 1,
                title: 1
            }
    },
    {
        $match:
            {
                "imdb.rating": {
                    $gt: 8
                },
                released_year: {
                    $gte: 2015,
                    $lte: 2023
                }
            }
    },
    {
        $count:
            "movie_count"
    }
])
// Ответ: 67


// Какой из них имеет самый высокий рейтинг ?
db.movies.aggregate([
    {
        $project:
            {
                released_year: {
                    $year: "$released"
                },
                "imdb.rating": 1,
                title: 1
            }
    },
    {
        $match:
            {
                "imdb.rating": {
                    $gt: 8
                },
                released_year: {
                    $gte: 2015,
                    $lte: 2023
                }
            }
    },
    {
        $sort:
            {
                "imdb.rating": -1
            }
    },
    {
        $limit:
            1
    }
])
// Ответ: "A Brave Heart: The Lizzie Velasquez Story", рейтинг - 9.4