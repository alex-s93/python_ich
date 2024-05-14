// 1. Тестовая коллекция в mongo atlas  sample_mflix.theaters
// Найти все кинотеатры в Калифорнии и посчитать их количество
db.theaters.aggregate([
    {
        $match: {
            "location.geo.coordinates": {
                $geoWithin: {
                    $geometry: {
                        type: "Polygon",
                        coordinates: [
                            [
                                [
                                    -124.30429995059968,
                                    42.04878275505149
                                ],
                                [
                                    -120.03185212612154,
                                    41.97336060215031
                                ],
                                [
                                    -120.12363731861116,
                                    38.9449943509411
                                ],
                                [
                                    -114.57328855991365,
                                    35.02886525059893
                                ],
                                [
                                    -114.65721085667612,
                                    32.743244646666305
                                ],
                                [
                                    -117.12714448571207,
                                    32.53389077782421
                                ],
                                [
                                    -120.49373991787436,
                                    34.421045302129116
                                ],
                                [
                                    -122.66797274351121,
                                    36.765468110461626
                                ],
                                [
                                    -124.78968858718873,
                                    40.12381912899715
                                ],
                                [
                                    -124.30429995059968,
                                    42.04878275505149
                                ]
                            ]
                        ]
                    }
                }
            }
        }
    },
    {
        $count:
        /**
         * Provide the field name for the count.
         */
            "theaters_count"
    }
])

db.theaters.countDocuments({"location.address.state": "CA"})
// Ответ: 169



// 2. Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews
// Найти недвижимость с самым большим количеством спален (bedrooms) и напишите ее название
db.airbnb.find({}, {name: 1, _id: 0}).sort({bedrooms: -1}).limit(1);
// Ответ: "Venue Hotel Old City".
// В этой недвижимости 20 комнат



// 3.Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews
// Найти недвижимость с самым высоким рейтингом  review_scores_rating при минимальном количестве отзывов 50
// (number_of_reviews) и напишите ее название
db.airbnb.find(
    {
        number_of_reviews: {$gte: 50}
    },
    {
        name: 1,
        _id: 0
    })
    .sort({
        'review_scores.review_scores_rating': -1,
        number_of_reviews: -1
    })
    .limit(1);
// я добавил дополнительно сортировку по количеству отзывов, чтобы вывелось имя максимально качественной недвижимости
// Ответ: 1分鐘到高鐵西九龍站､地鐵柯士甸站､機場和港珠澳大橋巴士A22站    10分鐘到中港城碼頭､海港城