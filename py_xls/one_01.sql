CREATE TABLE Loans (                -- Loans	таблиц€-дов≥дник по кредитам
        LoanId INT primary key,     -- (integer) LoanId	≥дентиф≥катор кредиту
        DisbursmentDate DATE,       -- DisbursmentDate	дата видач≥
        UserType bit,               -- UserType	≥дентиф≥катор типу кл≥Їнта
        -- FOREIGN KEY дл€ UserType (table UserTypes)
        -- св€зь с UserTypes
        Term TINYINT,               -- Term	терм≥н, на €кий видали кредит
        Amount DECIMAL(5,2),         -- Amount	сума кредиту
        FOREIGN KEY (UserType) REFERENCES UserTypes(UserType)
        );      
--	
--
--
-- UserTypes	таблиц€-дов≥дник по типам кл≥Їнт≥в
-- !!! ================================================
create table UserTypes (	            
         UserType BIT,                   -- UserType ≥дентиф≥катор типу кл≥Їнта
         UserTypeName VARCHAR(100) );    -- UserTypeName назва типу кл≥Їнта
         
--
--	
--Payments	таблиц€ факт≥в платеж≥в
create table Payments (
         PaymentId INT primary key,  --PaymentId	≥дентиф≥катор платежу
         LoanId int,                 --LoanId	≥дентиф≥катор кредиту
          -- св€зь с table Loans ==> LoanID
         PaidDate DATE,              -- PaidDate дата платежу
         Amount	DECIMAL(5,2),        -- Amount сума платежу
         FOREIGN KEY (LoanId) REFERENCES Loand(LoanId)
          ); 
         -- взаимодействие с суммой кредита
--	
-- sql_*, excel_0	вкладки ≥з завданн€ми
	
