CREATE TABLE Loans (                -- Loans	�������-������� �� ��������
        LoanId INT primary key,     -- (integer) LoanId	������������� �������
        DisbursmentDate DATE,       -- DisbursmentDate	���� ������
        UserType bit,               -- UserType	������������� ���� �볺���
        -- FOREIGN KEY ��� UserType (table UserTypes)
        -- ����� � UserTypes
        Term TINYINT,               -- Term	�����, �� ���� ������ ������
        Amount DECIMAL(5,2),         -- Amount	���� �������
        FOREIGN KEY (UserType) REFERENCES UserTypes(UserType)
        );      
--	
--
--
-- UserTypes	�������-������� �� ����� �볺���
-- !!! ================================================
create table UserTypes (	            
         UserType BIT,                   -- UserType ������������� ���� �볺���
         UserTypeName VARCHAR(100) );    -- UserTypeName ����� ���� �볺���
         
--
--	
--Payments	������� ����� �������
create table Payments (
         PaymentId INT primary key,  --PaymentId	������������� �������
         LoanId int,                 --LoanId	������������� �������
          -- ����� � table Loans ==> LoanID
         PaidDate DATE,              -- PaidDate ���� �������
         Amount	DECIMAL(5,2),        -- Amount ���� �������
         FOREIGN KEY (LoanId) REFERENCES Loand(LoanId)
          ); 
         -- �������������� � ������ �������
--	
-- sql_*, excel_0	������� �� ����������
	
