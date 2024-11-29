import math 
import statistics 
import numpy as np 
import pandas as pd 
from scipy.stats import norm 
from scipy.stats import binom 
from tabulate import tabulate 
import matplotlib.pyplot as plt 
from scipy.stats import poisson 
from scipy.stats import hypergeom 
from sklearn.linear_model import LinearRegression 
 
 
# ---------------------------------------------- Starting Decision ----------------------------------------------------- 
while True: 
 
    print("----------------------------------------- ( MAIN MENU ) -------------------------------------------------\n") 
    print("Press 1 -> Graphical and Tabular Representation\n") 
    print("Press 2 -> Descriptive Statistical Measure (Absolute & Relative)\n") 
    print("Press 3 -> Probability Methods/Distribution\n") 
    print("Press 4 -> Regression Modeling and Predictions and Regression estimates\n") 
    print("Press 5 -> End the Program\n") 
 
    x = int(input("Enter Choice: "))  # User Input 
 
    if x == 1:  # For Selecting Graphical and Tabular Representation---------------------------------------------------- 
        print("--------------------------------- ( TYPES OF REPRESENTATIONS ) --------------------------------------\n") 
        print("Press 1 -> Tabular Representation\n") 
        print("Press 2 -> Graphical Representation\n") 
        print("Press 3 -> Go Back\n") 
 
        x1 = int(input("Enter Choice: ")) 
 
        if x1 == 1:  # For Selecting Tabular Representation 
 
            # Ask the user for the data set (space-separated numbers) 
            data_input = input("Enter the data set (Quantitative data only, space-separated numbers): ") 
            data = [float(item) for item in data_input.split()] 
 
            # Calculate the frequency distribution using pandas 
            df = pd.DataFrame(data, columns=['Class']) 
            num_classes = 7 
 
            # Calculate the range of the data and the bin width for the histogram 
            data_range = max(data) - min(data) 
            bin_width = data_range / num_classes 
 
            # Create bins and labels for the histogram 
            bins = [min(data) + i * bin_width for i in range(num_classes + 1)] 
            labels = [f"{int(bins[i])}-{int(bins[i + 1])}" for i in range(num_classes)] 
 
            df['Class'] = pd.cut(df['Class'], bins=bins, labels=labels, right=False) 
            df = df.groupby('Class').size().reset_index(name='Frequency') 
            df['Cumulative Frequency'] = df['Frequency'].cumsum() 
            df['Relative Frequency'] = df['Frequency'] / df['Frequency'].sum() 
 
            # Display the frequency distribution table 
            print("\nFrequency Distribution Table:") 
            print(tabulate(df, headers='keys', tablefmt='grid', numalign='center')) 
 
        elif x1 == 2:  # For Selecting Graphical Representation 
 
            print("-------------------------------- ( GRAPHICAL REPRESENTATION ) -----------------------------------\n") 
            print("Press 1 -> Enter Data for Single Bar Chart\n") 
            print("Press 2 -> Enter Data for Multiple Bar Chart\n") 
            print("Press 3 -> Enter Data for Component Bar Chart\n") 
            print("Press 4 -> Enter Data for Pie Chart\n") 
            print("Press 5 -> Enter Data for Histogram\n") 
            print("Press 6 -> Enter Data for Box Plot\n") 
            print("Press 7 -> Go Back to Main Screen\n") 
 
            N = int(input("Enter Choice: ")) 
 
            if N == 1:  # For Single Bar Chart 
 
                data = {} 
                num_categories = int(input("Enter the number of categories: ")) 
 
                for i in range(num_categories): 
                    category_name = input(f"Enter the name of category {i + 1}: ") 
                    category_value = int(input(f"Enter the value for {category_name}: ")) 
                    data[category_name] = category_value 
 
                x_axis_label = input("Enter the name of X axis: ") 
                y_axis_label = input("Enter the name of Y axis: ") 
                plot_title = input("Enter the title of the plot: ") 
 
                categories = list(data.keys()) 
                values = list(data.values()) 
 
                fig = plt.figure(figsize=(10, 5)) 
                plt.bar(categories, values, color='maroon', width=0.4) 
 
                plt.xlabel(x_axis_label) 
                plt.ylabel(y_axis_label) 
                plt.title(plot_title) 
                plt.show() 
 
            elif N == 2:  # For Multi Bar Chart 
 
                categories = input("Enter the names of categories separated by spaces: ").split() 
                x_axis_label = input("Enter the name of X axis: ") 
                y_axis_label = input("Enter the name of Y axis: ") 
                plot_title = input("Enter the title of the plot: ") 
 
                var1 = input("Enter Name of Variable 1: ") 
                var2 = input("Enter Name of Variable 2: ") 
 
                Sample_A = [] 
                Sample_B = [] 
 
                for category in categories: 
                    s_A = int(input(f"Enter amount for {var1} in {category}: ")) 
                    Sample_A.append(s_A) 
 
                    s_B = int(input(f"Enter amount for {var2} in {category}: ")) 
                    Sample_B.append(s_B) 
 
                X_axis = np.arange(len(categories)) 
 
                plt.bar(X_axis - 0.2, Sample_A, 0.4, label=var1) 
                plt.bar(X_axis + 0.2, Sample_B, 0.4, label=var2) 
 
                plt.xticks(X_axis, categories) 
                plt.xlabel(x_axis_label) 
                plt.ylabel(y_axis_label) 
                plt.title(plot_title) 
                plt.legend() 
                plt.show() 
 
            elif N == 3:  # For Component/Stacked Bar Chart 
 
                num_categories = int(input("Enter the number of categories: ")) 
                x = [] 
                data = [] 
 
                for i in range(num_categories): 
                    category_name = input(f"Enter the name of category {i + 1}: ") 
                    x.append(category_name) 
 
                    category_data = np.array([int(score) for score in input( 
                        f"Enter the scores for {category_name} separated by spaces: ").split()]) 
                    data.append(category_data) 
 
                legend_labels = [input(f"Enter the label for round {i + 1}: ") for i in range(len(data))] 
                x_axis_label = input("Enter the name of X axis: ") 
                y_axis_label = input("Enter the name of Y axis: ") 
                plot_title = input("Enter the title of the plot: ") 
 
 
                fig, ax = plt.subplots() 
                bottom = np.zeros(len(x)) 
 
                for i, round_data in enumerate(data): 
                    ax.bar(x, round_data, bottom=bottom) 
                    bottom += round_data 
 
                plt.xlabel(x_axis_label) 
                plt.ylabel(y_axis_label) 
                plt.legend(legend_labels) 
                plt.title(plot_title) 
                plt.show() 
 
            elif N == 4:  # For Pie Chart 
 
                num_categories = int(input("Enter the number of categories: ")) 
                cars = [] 
                data = [] 
 
                for i in range(num_categories): 
                    car_name = input(f"Enter the name of category {i + 1}: ") 
                    cars.append(car_name) 
                    car_data = int(input(f"Enter the value for {car_name}: ")) 
                    data.append(car_data) 
 
                show_percentages = input( 
                    "Do you want to display percentages in the pie chart? (yes/no): ").lower() == 'yes' 
                title = input("Enter the title of the plot: ") 
 
                fig = plt.figure(figsize=(10, 7)) 
                _, texts, autotest = plt.pie(data, labels=cars, autopct='%1.1f%%' if show_percentages else None) 
 
                for text, autotext in zip(texts, autotest): 
                    text.set(color='white' if show_percentages else 'black') 
                    autotext.set(color='white' if show_percentages else 'black', size=10, weight='bold') 
 
                plt.title(title) 
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle. 
 
                # Adding legends and category names 
                plt.legend(labels=cars, title='Categories', loc='best') 
                plt.show() 
 
            elif N == 5:  # For Histogram 
 
                # Ask the user for the dataset 
                dataset = input("Enter the dataset (space-separated numbers): ") 
                data_points = [float(item) for item in dataset.split()] 
 
                # Ask the user for the title of the histogram 
                plot_title = input("Enter the title of the histogram: ") 
 
                # Creating histogram 
                fig, axs = plt.subplots(1, 1, figsize=(10, 7), tight_layout=True) 
                n_bins = 'auto'  # You can adjust this to change the number of bins 
 
                # Plot the histogram with customized appearance 
                axs.hist(data_points, bins=n_bins, color='green', edgecolor='black', alpha=0.7) 
 
                # Add x, y gridlines 
                axs.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5) 
 
                # Set background color 
                axs.set_facecolor('#f0f0f0') 
                 # Customize tick labels 
                axs.tick_params(axis='both', which='major', labelsize=12) 
                axs.tick_params(axis='both', which='minor', labelsize=10) 
 
                # Add a vertical line at the mean 
                mean_value = np.mean(data_points) 
                axs.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label='Mean') 
 
                # Add a vertical line at the median 
                median_value = np.median(data_points) 
                axs.axvline(median_value, color='blue', linestyle='dashed', linewidth=2, label='Median') 
 
                # Add legend 
                axs.legend(loc='upper right', fontsize=12) 
 
                # Adding extra features 
                plt.xlabel("X-axis", fontsize=14) 
                plt.ylabel("Frequency", fontsize=14) 
                plt.title(plot_title, fontsize=16) 
 
                # Show plot 
                plt.show() 
 
            elif N == 6:  # For Box Plot 
 
                # Ask the user for the title of the box plot 
                plot_title = input("Enter the title of the box plot: ") 
 
                # Ask the user for the data for the box plot (space-separated numbers) 
                data_input = input("Enter the data for the box plot (Quantitative data only): ") 
                data = [float(item) for item in data_input.split()] 
 
                # Creating box plot 
                fig = plt.figure(figsize=(10, 7)) 
                plt.boxplot(data) 
 
                # Calculate and add the mean as a red dot 
                mean_value = np.mean(data) 
                plt.plot(1, mean_value, marker='o', markersize=8, color='red', label='Mean') 
 
                # Adding extra features 
                plt.xlabel("Box Plot", fontsize=14) 
                plt.ylabel("Data Points", fontsize=14) 
                plt.title(plot_title, fontsize=16) 
                plt.legend() 
 
                # Show plot 
                plt.show() 
 
            elif N == 7:  # Break for Graphical Data 
                continue 
 
            else:  # This else ends Graphical Data 
                print("Invalid Entry") 
                continue 
        elif x1 == 3:  # Break for Choice between Graphical and Tabular 
            continue 
 
        else:  # This else ends the choice of tabular and graphical 
            print("Invalid Entry") 
            continue 
 
    elif x == 2:  # For Selecting Descriptive Statistical Measure (Absolute & Relative) ------------------------------
        while True: 
            print("---------------------------------- ( DESCRIPTIVE STATISTICS ) -----------------------------------\n") 
            print("Press 1 -> Mean\n") 
            print("Press 2 -> Median\n") 
            print("Press 3 -> Mode\n") 
            print("Press 4 -> Range\n") 
            print("Press 5 -> Variance\n") 
            print("Press 6 -> Standard Deviation\n") 
            print("Press 7 -> 3 Sigma Rule\n") 
            print("Press 8 -> Quartile 1,2,3\n") 
            print("Press 9 -> Inter quartile Range\n") 
            print("Press 10 -> Coefficient of Range\n") 
            print("Press 11 -> Coefficient of IQR\n") 
            print("Press 12 -> Coefficient of Variation\n") 
            print("Press 13 -> Go Back\n") 
 
            x = int(input("Enter Choice: ")) 
 
            if x == 1:  # IF STATEMENT FOR -MEAN- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(int, data_input.split())) 
                # Calculate the mean of the numbers 
                mean = statistics.mean(data) 
 
                # Print the result 
                print("Mean is:", mean) 
 
            elif x == 2:  # IF STATEMENT FOR -MEDIAN- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(int, data_input.split())) 
 
                # Calculate the median of the numbers 
                median = statistics.median(data) 
 
                # Print the result 
                print("Median is:", median) 
 
            elif x == 3:  # IF STATEMENT FOR -MODE- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(int, data_input.split())) 
 
                # Calculate the mode of the numbers 
                mode = statistics.mode(data) 
 
                # Print the result 
                print("Mode is:", mode) 
 
            elif x == 4:  # IF STATEMENT FOR -RANGE- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(int, data_input.split())) 
 
                # Calculate the range of the numbers 
                data_range = max(data) - min(data) 
 
                # Print the result 
                print("Range is:", data_range) 
 
            elif x == 5:  # IF STATEMENT FOR -VARIANCE- 
                 # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the variance of the numbers 
                variance = statistics.variance(data) 
 
                # Print the result 
                print("Variance is:", variance) 
 
            elif x == 6:  # IF STATEMENT FOR STANDARD -DEVIATION- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the standard deviation of the numbers 
                standard_deviation = statistics.stdev(data) 
 
                # Print the result 
                print("Standard Deviation is:", standard_deviation) 
 
            elif x == 7:  # IF STATEMENT FOR -3 SIGMA RULE- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the mean and standard deviation of the numbers 
                mean = statistics.mean(data) 
                standard_deviation = statistics.stdev(data) 
 
                # Calculate the lower and upper bounds for the 3-sigma rule 
                lower_bound = mean - 3 * standard_deviation 
                upper_bound = mean + 3 * standard_deviation 
 
                # Filter out the data points outside the 3-sigma range 
                data_within_3sigma = [x for x in data if lower_bound <= x <= upper_bound] 
                data_outside_3sigma = [x for x in data if x < lower_bound or x > upper_bound] 
 
                # Print the results 
                print("Data points within 3-sigma range:") 
                print(data_within_3sigma) 
                print("\nData points outside 3-sigma range:") 
                print(data_outside_3sigma) 
 
            elif x == 8:  # IF STATEMENT FOR -QUARTILE 1,2,3- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the quartiles 
                q1 = statistics.quantiles(data, n=4)[0] 
                q2 = statistics.median(data) 
                q3 = statistics.quantiles(data, n=4)[2] 
 
                # Print the results 
                print("Q1 (25th percentile):", q1) 
                print("Q2 (Median, 50th percentile):", q2) 
                print("Q3 (75th percentile):", q3) 
 
            elif x == 9:  # IF STATEMENT FOR -INTER QUARTILE RANGE- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the quartiles 
                q1 = statistics.quantiles(data, n=4)[0] 
                q3 = statistics.quantiles(data, n=4)[2] 
 
                # Calculate the Inter quartile Range (IQR) 
                iqr = q3 - q1 
 
                # Print the result 
                print("Inter quartile Range (IQR):", iqr) 
 
            elif x == 10:  # IF STATEMENT FOR -CO-EFFICIENT OF RANGE- 
 
                # Ask the user to input a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the coefficient of range 
                data_range = max(data) - min(data) 
                coefficient_of_range = (data_range / (max(data) + min(data))) * 100 
                 # Print the result 
                print("Coefficient of Range:", coefficient_of_range) 
 
            elif x == 11:  # IF STATEMENT FOR -CO-EFFICIENT OF IQR- 
 
                # Ask the user for a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the first quartile (Q1), second quartile (Q2 or median), and third quartile (Q3) 
                q1 = np.percentile(data, 25) 
                q2 = np.percentile(data, 50) 
                q3 = np.percentile(data, 75) 
 
                # Calculate the inter quartile range (IQR) 
                iqr = q3 - q1 
 
                # Calculate the coefficient of IQR 
                coefficient_of_iqr = (iqr / (q3 + q1)) * 100 
 
                # Print the results 
                print("Coefficient of IQR:", coefficient_of_iqr) 
 
            elif x == 12:  # IF STATEMENT FOR CO-EFFICIENT OF VARIANCE- 
 
                # Ask the user for a list of numbers (space-separated) 
                data_input = input("Enter a list of numbers (space-separated): ") 
                data = list(map(float, data_input.split())) 
 
                # Calculate the standard deviation 
                std_deviation = np.std(data) 
 
                # Calculate the mean (x-bar) 
                mean = np.mean(data) 
 
                # Calculate the coefficient of variance 
                coefficient_of_variance = (std_deviation / mean) * 100 
 
                # Print the results 
                print("Coefficient of Variance:", coefficient_of_variance) 
            elif x == 13: 
                break 
            else: 
                print("Invalid Entry") 
 
            input("Press any key to continue...")  # Pausing 
 
    elif x == 3:  # Probability Methods/Distribution-------------------------------------------------------------------- 
 
        print("------------------------------- ( PROBABILITY METHODS/DISTRIBUTIONS ) -------------------------------\n") 
        print("Press 1 -> Simple Probability\n") 
        print("Press 2 -> Counting Technique\n") 
        print("Press 3 -> Factorial Method\n") 
        print("Press 4 -> Multiplicative Technique\n") 
        print("Press 5 -> Permutation\n") 
        print("Press 6 -> Combination\n") 
        print("Press 7 -> Binomial Probability Distribution\n") 
        print("Press 8 -> Poison Probability Distribution\n") 
        print("Press 9 -> Hyper-geometric Probability Distribution\n") 
        print("Press 10 -> Uniform Probability Distribution (Standardization)\n") 
        print("Press 11 -> Covariance\n") 
        print("Press 12 -> Correlation\n") 
        print("Press 13 -> Go Back\n") 
 
        val = int(input("Enter Choice: ")) 
 
        if val == 1:  # IF STATEMENT FOR -SIMPLE PROBABILITY- 
 
            favourable_outcome = float(input("Enter Favourable Outcome: ")) 
            total_outcome = float(input("Enter Total Outcomes: ")) 
 
            if favourable_outcome <= 0 or total_outcome <= 0: 
                print("Invalid Entry") 
                continue 
            if favourable_outcome > total_outcome:  # Check for invalid Entry 
                print("Favourable cannot be greater then Total Outcome") 
                continue 
 
            result = favourable_outcome / total_outcome 
            print("Simple Probability:", result) 
 
        elif val == 2:  # IF STATEMENT FOR -COUNTING TECHNIQUE- 
 
            m1 = int(input("Enter Possible Outcome m1: ")) 
            m2 = int(input("Enter Possible Outcome m2: ")) 
            result = m1 * m2 
            print("Total Number of Possibilities:", result) 
 
        elif val == 3:  # IF STATEMENT FOR -FACTORIAL METHOD- 
 
            objects = int(input("Enter Objects: ")) 
            arrangements = int(input("Enter Arrangements: ")) 
 
            if objects != arrangements: 
                print("Invalid Entry") 
                continue 
 
            result = math.factorial(objects)  # Calculate the factorial using the built-in function 
 
            # Print the result 
            print(f"Total Number of arrangements: {result}") 
 
        elif val == 4:  # IF STATEMENT FOR -MULTIPLICATIVE TECHNIQUE- 
 
            # Ask the user for the values of n and r 
            N = int(input("Enter the value of n (total objects): ")) 
            r = int(input("Enter the value of r (arrangements): ")) 
 
            arrangements = math.perm(N, r)  # Calculate the number of permutations (arrangements) 
 
            print(f"Number of arrangements: {arrangements}") 
 
        elif val == 5:  # IF STATEMENT FOR PERMUTATION 
 
            N = int(input("Enter the value of n (total objects): ")) 
            r = int(input("Enter the value of r (arrangements): ")) 
 
            permutations = math.perm(N, r)  # Calculate the number of permutations 
 
            print(f"Number of permutations: {permutations}") 
 
        elif val == 6:  # IF STATEMENT FOR COMBINATION 
 
            N = int(input("Enter the value of n (total objects): ")) 
            r = int(input("Enter the value of r (combinations): ")) 
 
            combinations = math.comb(N, r)  # Calculate the number of combinations 
 
            print(f"Number of combinations: {combinations}") 
        elif val == 7:  # IF STATEMENT FOR -BINOMIAL PROBABILITY DISTRIBUTION- 
 
            # Ask the user for the values of n, p, and k 
            N = float(input("Enter the number of trials (n): ")) 
            P = float(input("Enter the probability of success in each trial (p): ")) 
            X = float(input("Enter the number of successes (k): ")) 
 
            if N < 0 or P < 0 or X < 0 or P > 1:  # Check for Invalid Entry 
                print("Invalid Entry") 
                continue 
 
            probability = binom.pmf(X, N, P)  # Calculate the binomial probability mass function 
            expected_value_binomial = N * P  # Calculate Expected Value 
            variance_b = (N * P) / 1 - P  # Calculate Variance 
            standard_b = math.sqrt(variance_b)  # Calculate Standard Deviation 
 
            print(f"\nThe probability of getting exactly {X} successes in {N} trials with a success probability of " 
                  f"{P} is: {probability:.5f}") 
            print(f"Expected Value: {expected_value_binomial}") 
            print(f"Variance Value: {variance_b}") 
            print(f"Standard Deviation Value: {standard_b}\n") 
 
        elif val == 8:  # IF STATEMENT FOR -POISON PROBABILITY DISTRIBUTION- 
 
            N_ = float(input("Enter the number of trials (n): ")) 
            P_ = float(input("Enter the probability of success in each trial (p): ")) 
            # Ask the user for the specific value (k) for which to calculate the probability 
            k = float(input("Enter the number of events (k): ")) 
 
            if N_ < 100 or P_ > 0.1:  # Check for n >= 100 and p <= 0.1 
                print("Invalid Entry") 
                continue 
 
            lamda = N_ * P_  # Calculating Average (lambda) for Poisson distribution 
 
            probability = poisson.pmf(k, lamda)  # Calculate the Poisson probability mass function 
            expectedValue_poi = lamda 
            variance_poi = lamda 
            standard_poi = math.sqrt(variance_poi) 
 
            print(f"The probability of getting exactly {k} events with an average rate of {lamda:.5f} " 
                  f"is: {probability:.5f}") 
            print(f"Expected Value: {expectedValue_poi:.5f}") 
            print(f"Variance Value: {variance_poi:.5f}") 
            print(f"Standard Deviation Value: {standard_poi:.5f}\n") 
 
        elif val == 9:  # IF STATEMENT FOR -HYPER GEOMETRIC PROBABILITY DISTRIBUTION- 
 
            N = int(input("Enter the population size (N): ")) 
            M = int(input("Enter the number of successes in the population (M): ")) 
            n = int(input("Enter the number of trials (n): ")) 
            k = int(input("Enter the number of successes in the sample (k): ")) 
 
            if N <= 0 or M < 0 or n <= 0 or k < 0 or M > N or k > n or M < n:  # Check for invalid entry 
                print("Invalid Entry") 
                continue 
 
            probability = hypergeom.pmf(k, N, M, n)  # Calculate the Hyper-geometric probability mass function 
            expectedValue_hyper = (n * M) / N  # Calculation of expected value 
            variance_hyper = ((n * M) / (N - 1)) * ((N - n) / (N - 1)) * ((N - M) / N)  # Calculation of Variance 
            standard_hyper = math.sqrt(variance_hyper) 
 
            print(f"The probability of getting exactly {k} successes in {n} trials with a population size of {N} " 
                  f"and {M} successes in the population is: {probability:.5f}") 
            print(f"Expected Value: {expectedValue_hyper:.5f}") 
            print(f"Variance Value: {variance_hyper:.5f}") 
            print(f"Standard Deviation Value: {standard_hyper:.5f}\n") 
 
        elif val == 10:  # IF STATEMENT FOR UNIFORM DISTRIBUTION 
 
            value_x = float(input("Enter Value of x: ")) 
            mean_x = float(input("Enter Mean: ")) 
            std_x = float(input("Enter Standard Deviation: ")) 
 
            z_score = (value_x - mean_x)/std_x 
 
            # Calculate the p-value (probability) corresponding to the Z-score 
            p_value = 1 - norm.cdf(z_score) 
 
            print("Z-score:", z_score) 
            print("p-value:", p_value) 
 
        elif val == 11:  # IF STATEMENT FOR CO-VARIANCE 
 
            # Get user input for data points 
            print("Enter the data points for X and Y in the format 'x1,x2,...,y'. Type 'done' to stop.") 
            data_points = [] 
            while True: 
                point = input("Data point: ") 
                if point.lower() == 'done': 
                    break 
                try: 
                    data = list(map(float, point.split(','))) 
                    data_points.append(data) 
                except ValueError: 
                    print("Invalid input! Please try again.") 
 
            # Convert data_points to numpy array 
            data_points = np.array(data_points) 
 
            # Extract X and Y values from data_points 
            X = data_points[:, :-1] 
            Y = data_points[:, -1] 
 
            # Calculate the covariance 
            n = len(X) 
            mean_x = sum(X) / n 
            mean_y = sum(Y) / n 
 
            cov = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n)) / n 
 
            # Print the direction of the relationship based on covariance value 
            if cov[0] < 0: 
                print("Inverse relation: As one variable increases, the other tends to decrease.") 
            elif cov[0] > 0: 
                print("Direct relation: As one variable increases, the other tends to increase.") 
            else: 
                print("No linear relation: The variables show no consistent linear relationship.") 
 
            print(f"Covariance: {cov[0]}") 
 
        elif val == 12:  # IF STATEMENT FOR CO-RELATION 
 
            # Get user input for data points 
            print("Enter the data points for X and Y in the format 'x1,x2,...,y'. Type 'done' to stop.") 
            data_points = [] 
            while True: 
                point = input("Data point: ") 
                if point.lower() == 'done': 
                    break 
                try: 
                    data = list(map(float, point.split(','))) 
                    data_points.append(data) 
                except ValueError: 
                    print("Invalid input! Please try again.") 
 
            # Convert data_points to numpy array 
            data_points = np.array(data_points) 
 
            # Extract X and Y values from data_points 
            X = data_points[:, :-1] 
            Y = data_points[:, -1] 
 
            mean_X = np.mean(X) 
            mean_Y = np.mean(Y) 
 
            # Calculate the covariance 
            cov_x_and_y = np.dot((X - mean_X).T, Y - mean_Y) / len(X) 
 
            # Calculate the correlation coefficient 
            std_dev_X = np.std(X) 
            std_dev_Y = np.std(Y) 
            correlation_coefficient = cov_x_and_y / (std_dev_X * std_dev_Y) 
 
            # Extract the correlation coefficient value 
            corr_value = correlation_coefficient[0] 
 
            # Print the strength of the relationship based on correlation coefficient 
            if corr_value == 0: 
                print("No relation: The variables show no consistent linear relationship.") 
            elif 0 < abs(corr_value) < 0.1: 
                print("Very weak relation: The variables have a very weak linear relationship.") 
            elif 0.1 <= abs(corr_value) < 0.3: 
                print("Weak relation: The variables have a weak linear relationship.") 
            elif 0.3 <= abs(corr_value) < 0.5: 
                print("Moderate relation: The variables have a moderate linear relationship.") 
            elif 0.5 <= abs(corr_value) < 0.8: 
                print("Good relation: The variables have a good linear relationship.") 
            elif 0.8 <= abs(corr_value) < 0.9: 
                print("Excellent relation: The variables have an excellent linear relationship.") 
            elif abs(corr_value) >= 0.9: 
                print("Exact relation: The variables have an exact linear relationship.") 
 
            print("Correlation Coefficient:", corr_value) 
        elif val == 13: 
            continue 
        else: 
            print("Invalid Entry\n") 
            continue 
 
    elif x == 4: 
 
        print("\n------------------------------- (Regression Modeling and Predictions and Regression estimates)" 
              " -------------------------------\n") 
        print("Press 1 -> Simple Linear Regression Model\n") 
        print("Press 2 -> Multiple Linear Regression Model\n") 
        print("Press 3 -> Go Back\n") 
 
        e = int(input("Enter Choice:")) 
 
        if e == 1:  # IF STATEMENT FOR LINEAR REGRESSION MODEL 
 
            # Get user input for data points 
            print("Enter the data points in the format 'x,y'. Type 'done' to stop.") 
            data_points = [] 
            while True: 
 
                point = input("Data point: ") 
                if point.lower() == 'done': 
                    break 
                try: 
                    x, y = map(float, point.split(',')) 
                    data_points.append((x, y)) 
                except ValueError: 
                    print("Invalid input! Please try again.") 
 
            # Convert data_points to numpy arrays 
            data_points = np.array(data_points) 
 
            # Extract x and y values from data_points 
            x = data_points[:, 0] 
            y = data_points[:, 1] 
 
            # Visualize the data points 
            plt.scatter(x, y, color='blue', label='Data points') 
            plt.xlabel('X') 
            plt.ylabel('Y') 
            plt.title('User Input Data Points') 
            plt.legend() 
            plt.show() 
 
            # Reshape x to 2D array 
            x = x.reshape(-1, 1) 
 
            # Fit a linear regression model 
            model = LinearRegression() 
            model.fit(x, y) 
 
            # Visualize the linear regression line 
            plt.scatter(x, y, color='blue', label='Data points') 
            plt.plot(x, model.predict(x), color='red', label='Linear regression line') 
            plt.xlabel('X') 
            plt.ylabel('Y') 
            plt.title('Linear Regression') 
            plt.legend() 
            plt.show() 
 
            # Get user input for prediction 
            while True: 
                x_value = input("Enter a value of X for prediction (type 'exit' to stop): ") 
                if x_value.lower() == 'exit': 
                    break 
                try: 
                    x_prediction = float(x_value) 
                    y_prediction_value = model.predict([[x_prediction]]) 
                    print(f"Predicted Y for X = {x_prediction}: {y_prediction_value[0]}") 
                except ValueError: 
                    print("Invalid input! Please enter a numeric value or type 'exit' to stop.") 
 
        elif e == 2:  # IF STATEMENT FOR MULTIPLE LINEAR REGRESSION MODEL 
 
            # Get user input for data points 
            print("Enter the data points in the format 'x1,x2,...,y'. Type 'done' to stop.") 
            data_points = [] 
            while True: 
                point = input("Data point: ") 
                if point.lower() == 'done': 
                    break 
                try: 
                    data = list(map(float, point.split(','))) 
                    data_points.append(data) 
                except ValueError: 
                    print("Invalid input! Please try again.") 
 
            # Convert data_points to numpy array 
            data_points = np.array(data_points) 
 
            # Extract X and y values from data_points 
            X = data_points[:, :-1] 
            y = data_points[:, -1] 
 
            # Visualize the data points 
            fig = plt.figure() 
            ax = fig.add_subplot(111, projection='3d') 
            ax.scatter(X[:, 0], X[:, 1], y, c='b', marker='o') 
            ax.set_xlabel('X1') 
            ax.set_ylabel('X2') 
            ax.set_zlabel('Y') 
            plt.title('User Input Data Points') 
            plt.show() 
 
            # Fit a multiple linear regression model 
            model = LinearRegression() 
            model.fit(X, y) 
 
            # Get user input for prediction 
            while True: 
                try: 
                    input_values = input( 
                        "Enter values of X1 and X2 for prediction separated by a comma (type 'exit' to stop): ") 
                    if input_values.lower() == 'exit': 
                        break 
                    x1, x2 = map(float, input_values.split(',')) 
                    x_prediction_value = np.array([[x1, x2]]) 
                    y_prediction_value = model.predict(x_prediction_value) 
                    print(f"Predicted Y for X1 = {x1}, X2 = {x2}: {y_prediction_value[0]}") 
                except ValueError: 
                    print("Invalid input! Please enter numeric values separated by a comma or type 'exit' to stop.") 
    elif x == 5: 
        print("Program Ended\n") 
        break 
    else: 
        print("Invalid Entry\n") 
input("Press any key to continue...")  # Pausing