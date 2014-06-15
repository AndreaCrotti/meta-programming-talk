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


;; http://cl-cookbook.sourceforge.net/macros.html
; possible implementation of a for loop using a macro

(defmacro for (listspec exp)
   (cond ((and (= (length listspec) 3)    ; list has three elements
               (symbolp (car listspec))   ; first element is a symbol
               (eq (cadr listspec) ':in)) ; second element is symbol :in
          `(mapcar (lambda (,(car listspec)) ; Map the expression to the list
                      ,exp)
                   ,(caddr listspec)))
         (t (error "Ill-formed: %s" `(for ,listspec ,exp)))))

(for (x :in l)
   (let ((y (hairy-fun1 x)) (z (hairy-fun2 x)))
      (dolist (y1 y)
         (dolist (z1 z) 
           
           ))))


