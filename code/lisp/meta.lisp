;; http://kuomarc.wordpress.com/2012/02/02/why-i-love-common-lisp-and-hate-java-part-ii-code-examples/

(defun get-from-list(list pred)
  (let ((ans (first list)))
    (do ((i 1 (1+ i)))
        ((>= i (length list)) ans)
      (when (funcall pred (nth i list) ans)
        (setf ans (nth i list))))))

(defun get-max(list)
  (get-from-list list #'>))

(defun get-min(list)
  (get-from-list list #'<))

(defmacro get-from-list(list pred)
  `(let ((ans (first ,list)))
     (do ((i 1 (1+ i)))
         ((>= i (length ,list)) ans)
       (when (,pred (nth i ,list) ans)
         (setf ans (nth i ,list))))))


(defun get-max(list)
  ;TODO: small difference but very important
  (get-from-list list >))

(defun get-min(list)
  (get-from-list list <))


;TODO: define your own loop or add some smart syntax
