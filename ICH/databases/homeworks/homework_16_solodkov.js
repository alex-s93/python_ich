// Найдите средний возраст из коллекции ich.US_Adult_Income
db.US_Adult_Income.aggregate([
    {
        $group:
            {
                _id: null,
                avg_age: {
                    $avg: "$age"
                }
            }
    }
])

// Поменяв подключение к базе данных, создать коллекцию orders_NAME (для уникальности - добавим ваше имя в название)
// со свойствами id, customer, product, amount, city, используя следующие данные:
//
// 1 Olga Apple 15.55 Berlin
// 2 Anna Apple 10.05 Madrid
// 3 Olga Kiwi 9.6 Berlin
// 4 Anton Apple 20 Roma
// 5 Olga Banana 8 Madrid
// 6 Petr Orange 18.3 Paris

db.Orders_190224_ptm_Solodkov.insertMany([
    {
        id: 1,
        customer: "Olga",
        product: "Apple",
        amount: 15.55,
        city: "Berlin"
    },
    {
        id: 2,
        customer: "Anna",
        product: "Apple",
        amount: 10.05,
        city: "Madrid"
    },
    {
        id: 3,
        customer: "Olga",
        product: "Kiwi",
        amount: 9.6,
        city: "Berlin"
    },
    {
        id: 4,
        customer: "Anton",
        product: "Apple",
        amount: 20,
        city: "Roma"
    },
    {
        id: 5,
        customer: "Olga",
        product: "Banana",
        amount: 8,
        city: "Madrid"
    },
    {
        id: 6,
        customer: "Petr",
        product: "Orange",
        amount: 18.3,
        city: "Paris"
    }
])

// Найти сколько всего было совершено покупок
db.Orders_190224_ptm_Solodkov.countDocuments()
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $count: "order_count"
    }
])

// Найти сколько всего раз были куплены яблоки
db.Orders_190224_ptm_Solodkov.countDocuments({product: "Apple"})
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $match: {
            product: "Apple"
        }
    },
    {
        $count: "order_count"
    }
])

// Вывести идентификаторы трех самые дорогих покупок
db.Orders_190224_ptm_Solodkov.find({}, {id: 1}).sort({amount: -1}).limit(3)
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $sort:
            {
                amount: -1
            }
    },
    {
        $limit:
            3
    },
    {
        $project:
            {
                id: 1,
                _id: 0
            }
    }
])

// Найти сколько всего покупок было совершено в Берлине
db.Orders_190224_ptm_Solodkov.countDocuments({city: "Berlin"})
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $match: {
            city: "Berlin"
        }
    },
    {
        $count: "order_count"
    }
])

// Найти количество покупок яблок в городах Берлин и Мадрид
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $match:
            {
                $and: [
                    {
                        product: "Apple"
                    },
                    {
                        city: {
                            $in: ["Berlin", "Madrid"]
                        }
                    }
                ]
            }
    },
    {
        $count: "order_count"
    }
])

// Найти сколько было потрачено каждым покупателем
//     (подсказка: используем $group и total: {$sum: '$amount'} )
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $group:
            {
                _id: "$customer",
                total: {
                    $sum: "$amount"
                }
            }
    }
])

// Найти в каких городах совершала покупки Ольга
//     (подсказка: используем $match customer: 'Olga' и $group _id: '$city')
db.Orders_190224_ptm_Solodkov.aggregate([
    {
        $match: {
            customer: "Olga"
        }
    },
    {
        $group: {
            _id: "$city"
        }
    }
])