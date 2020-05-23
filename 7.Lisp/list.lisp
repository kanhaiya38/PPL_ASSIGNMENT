(princ "Enter number of elements in list: ")

(setq x (read))
(setq y (list))

(princ "Enter the elements of list: ")

(loop for i from 0 to (- x 1)
      do(
	setq y (append y (list(read)))
	)
      )

(princ "Enter the value of n: ")
(setq i (read))

(write i)
(princ "th element of list is : ")
(princ (nth (- i 1) y))
