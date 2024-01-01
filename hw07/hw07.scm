(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((< num 0) -1)
    ((= num 0) 0)
    (else 1))
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond ((= y 0) 1)
    ((= y 1) x)
    ((odd? y) (square (pow x (/ y 2))))
    (else (* x (square (pow x (/ (- y 1) 2)))))))

(define (unique s)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s))))(cdr s)))))
)

;尾递归需要再定义一个函数，要存储功能的话就要将存储表作为参数传
(define (replicate x n)
  'YOUR-CODE-HERE
  (define (repl lst x n)
    (if (= n 0)
      lst
      (repl (cons x lst) x (- n 1))))
  (repl nil x n)
  )


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (begin
    (define (acc result combiner start n term)
      (if (= n 0)
        result
        (acc (combiner (term start) result) combiner (+ 1 start) (- n 1) term)))
    (acc start combiner 1 n term)
  )
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (begin
    (define (acc result combiner start n term)
      (if (= n 0)
        result
        (acc (combiner (term start) result) combiner (+ 1 start) (- n 1) term)))
    (acc start combiner 1 n term)
  )
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)

