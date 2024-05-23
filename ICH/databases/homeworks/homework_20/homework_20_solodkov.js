// 6. Найти рестораны на 'Staten Island' в названии которых есть слово pizza (Pizza и PIZZA тоже считаются)
db.restaurants.find({borough: "Staten Island", name: /\bpizza\b/i})

// 7. Выведите названия 5 лучших по среднему значению отзывов ( $avg: "$grades.score")
db.restaurants.aggregate([
    {
        $unwind: {
            path: "$grades"
        }
    },
    {
        $group: {
            _id: "$name",
            avg_score: {
                $avg: "$grades.score"
            }
        }
    },
    {
        $project:
            {
                name: "$_id",
                avg_score: 1,
                _id: 0
            }
    },
    {
        $sort: {
            avg_score: -1
        }
    },
    {
        $limit: 5
    }
])