def get_interactive_answer(errors_num):
    print(f'Found {errors_num} errors, show solutions in browser?(y - yes, n - no): ')
    answer = input()
    return answer == 'y'
