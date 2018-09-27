import argparse
import main as m

parser = argparse.ArgumentParser()
parser.add_argument('type', help='type can be [initialize/recommend-products]')
initialize = parser.add_argument_group('initialize')
initialize.add_argument('--users-file', '-u', nargs=1, help='users file')
initialize.add_argument('--products-file', '-p', nargs=1, help='products file')
initialize.add_argument('--current-timestamp', '-ct', nargs=1, help='timestamp')
recommend_products = parser.add_argument_group('recommend-products')
recommend_products.add_argument('--user-id', '-uid', help='write your uid', nargs=1, default=['12342'])

args = parser.parse_args()

if args.type == 'initialize' and args.users_file != None and args.products_file != None and args.current_timestamp != None:
    m.scoringFunc(args.users_file.pop(), args.products_file.pop(), int(args.current_timestamp.pop()))
    print('initialize completed')
elif args.type == 'initialize' and (args.users_file == None or args.products_file == None or args.current_timestamp == None):
    parser.print_help()
elif args.type == 'recommend-products' and args.user_id != None:
    m.recommend(args.user_id.pop())
elif args.type == 'recommend-products' and args.user_id == None:
    parser.print_help()
elif args.type != 'initialize' or args.type != 'recommend-products':
    parser.print_help()
