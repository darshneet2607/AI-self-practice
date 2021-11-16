;;;;To print nth number in rth row of a pascal's traingle
(defun pascal (n r)
  (if (= n 1) 1
    (if (= n r) 1
      (+ (pascal (- n 1) (- r 1)) (pascal n (- r 1)))
    )
   )
)
(princ (pascal 3 5))