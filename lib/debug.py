from department import Department

# Reset the table
Department.drop_table()
Department.create_table()

# Create and save departments
dept1 = Department("Engineering")
dept1.save()
print(dept1)  # Should print with an ID

dept2 = Department.create("Marketing")
print(dept2)

# Update a department
dept1.name = "Software Engineering"
dept1.save()
print(dept1)

# Find by id
found = Department.find_by_id(dept1.id)
print(found)

# Get all departments
all_depts = Department.get_all()
print(all_depts)

# Delete
dept2.delete()
print(Department.get_all())
