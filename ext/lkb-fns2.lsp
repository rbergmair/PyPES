(in-package :mrs)



(defun simple-io-mrsfs-to-xmlrmrs (istream ostream)

  (setf (stream-external-format istream) :utf-8)
  (setf (stream-external-format ostream) :utf-8)
  (setq excl::*global-gc-behavior* :auto)

  (common-lisp-user::simple-io-write-delim ostream)
  (finish-output ostream)

  (loop

    (setq input (common-lisp-user::simple-io-read-block istream))

    (if (not input)
      (return))

    (with-input-from-string (jstream input)
      (setf (stream-external-format jstream) :utf-8)
      (setq imrs (read-mrs jstream))
      (setq robmrs (mrs-to-rmrs imrs))
      (output-rmrs1 robmrs 'mrs::xml ostream)
      (common-lisp-user::simple-io-write-delim ostream)
      (finish-output ostream)
    )

  )

)



(defun simple-io-mrsfs-to-xmlmrs (istream ostream)

  (setf (stream-external-format istream) :utf-8)
  (setf (stream-external-format ostream) :utf-8)
  (setq excl::*global-gc-behavior* :auto)

  (common-lisp-user::simple-io-write-delim ostream)
  (finish-output ostream)

  (loop

    (setq input (common-lisp-user::simple-io-read-block istream))

    (if (not input)
      (return))

    (with-input-from-string (jstream input)
      (setf (stream-external-format jstream) :utf-8)
      (setq imrs (read-mrs jstream))
      (output-mrs1 imrs 'mrs-xml ostream)
      (common-lisp-user::simple-io-write-delim ostream)
      (finish-output ostream)
    )

  )

)



(defun simple-io-mrsfs-to-scopedmrs (istream ostream)

  (setf (stream-external-format istream) :utf-8)
  (setf (stream-external-format ostream) :utf-8)
  (setq excl::*global-gc-behavior* :auto)
  
  (setf mrs::*scoping-call-limit* 262144)

  (common-lisp-user::simple-io-write-delim ostream)
  (finish-output ostream)

  (loop

    (setq input (common-lisp-user::simple-io-read-block istream))

    (if (not input)
      (return))

    (with-input-from-string (jstream input)

      (setf (stream-external-format jstream) :utf-8)
      (setq imrs (read-mrs jstream)
)
      (setq scopes (make-scoped-mrs imrs))
      
      (loop
        for scope in scopes
        do
          (setf *canonical-bindings* 
                (canonical-bindings scope))
          (mrs::output-scoped-mrs 
            imrs :stream ostream)
        finally
          (setf *canonical-bindings* nil))
      
      (common-lisp-user::simple-io-write-delim ostream)
      (finish-output ostream)
    )

  )

)



(defun simple-io-mrsread4 (istream ostream)

  (setf (stream-external-format istream) :utf-8)
  (setf (stream-external-format ostream) :utf-8)
  (setq excl::*global-gc-behavior* :auto)
  
  (setf mrs::*scoping-call-limit* 262144)

  (common-lisp-user::simple-io-write-delim ostream)
  (finish-output ostream)

  (loop

    (setq input (common-lisp-user::simple-io-read-block istream))

    (if (not input)
      (return))

    (with-input-from-string (jstream input)

      (setf (stream-external-format jstream) :utf-8)
      (setq imrs (read-mrs jstream)
)
      (setq scopes (make-scoped-mrs imrs))
      
      (loop
        for scope in scopes
        do
          (setf *canonical-bindings* 
                (canonical-bindings scope))
          (mrs::output-fol-approximation
            imrs ostream)
        finally
          (setf *canonical-bindings* nil))
      
      (common-lisp-user::simple-io-write-delim ostream)
      (finish-output ostream)
    )

  )

)
