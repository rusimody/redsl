data Symbol = MSFT | GOOG | IBM | APL | AT deriving (Show, Eq)

data Series = A | B | C | D | E | F | G deriving (Show, Eq)

data SerType = Plain | Preferred | Warrant deriving (Eq)

type Issued = Bool

type Suffix = (Maybe SerType, Maybe Series, Issued)

type Symbolology = (Symbol, Suffix)


-- (Scrip, (SerType, Series, Issued))
-- Yes this can be made a cleaner record type in haskell (not gofer)
-- Nesting of suffix can be removed

 
serialize :: Symbolology -> String
serialize (scr,suf) = show scr ++ serializesuf suf

serializesuf (Just st,Just ser,i) = show st ++ show ser ++ serializeiss i
serializesuf (Just st,Nothing,i)   = show st ++ serializeiss i
serializesuf (Nothing,Just ser,i) = show ser ++ serializeiss i
serializesuf (Nothing,Nothing,i)   = serializeiss i

serializeiss True  = "#"
serializeiss False = ""

instance Show SerType where
  showsPrec _ Plain	= showString " "
  showsPrec _ Preferred = showString "-"
  showsPrec _ Warrant	= showString "+"

--

sym1 = "IBM A#"
sym1repr = (IBM, (Plain, Just A, True))
