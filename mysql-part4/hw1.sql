SELECT book.title, author.name, genre.name, book.price, book.amount
FROM book
INNER JOIN author ON author.id = book.author_id
INNER JOIN genre ON genre.id = book.genre_id
WHERE amount = (SELECT MAX(amount) FROM book)
ORDER BY book.title;
