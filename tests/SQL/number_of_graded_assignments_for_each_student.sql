-- Write query to get number of graded assignments for each student:
select student_id,COUNT(*) FROM assignments WHERE state = 'GRADED' Group By student_id;