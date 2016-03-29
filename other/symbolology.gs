data Symbol = MSFT | GOOG | IBM | APL | AT

data Series = A | B | C | D | E | F | G

data SerType = Plain | Preferred | Warrant

type Issued = Bool

data Maybe.a = Ok.a | None

type Suffix = (Maybe.SerType, Maybe.Series, Issued)

type Symbolology = (Symbol, Suffix)

-- (Scrip, (SerType, Series, Issued))
-- Nesting of suffix can be removed

 
serialize : Symbolology -> String
serialize.(scr,suf) = show.scr ++ serializesuf.suf

serializesuf.(Ok.st,Ok.ser,i) = show.st ++ show.ser ++ serializeiss.i
serializesuf.(Ok.st,None,i)   = show.st ++ serializeiss.i
serializesuf.(None,Ok.ser,i) = show.ser ++ serializeiss.i
serializesuf.(None,None,i)   = serializeiss.i


serializeiss.True  = "#"
serializeiss.False = ""

--
--
-- Some messy stuff below -- Ignore!

instance Text Symbol
-- instance Text.a => Text.(Maybe.a)

instance Text Series

instance Text SerType where
  showsPrec._.Plain	= showString."."
  showsPrec._.Preferred = showString."-"
  showsPrec._.Warrant	= showString."+"

--

sym1 = "IBM.A#"
sym1repr = (IBM, (Plain, Ok.A, True))
