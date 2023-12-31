from constraint import Problem

def main():
    problem = Problem()

    regions = input("Enter the names of regions (comma-separated): ").split(',')
    colors = input("Enter the colors (comma-separated): ").split(',')

    for region in regions:
        problem.addVariable(region.strip(), colors)

    num_constraints = int(input("Enter the number of adjacency constraints: "))
    for _ in range(num_constraints):
        region1, region2 = input("Enter adjacent regions (region1 region2): ").split()
        problem.addConstraint(lambda r1, r2: r1 != r2, (region1, region2))
    
    solutions = problem.getSolutions()

    print("Possible solutions:")
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
