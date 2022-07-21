#!/bin/python3
import dns.resolver
import sys
records_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
try:
    domain = sys.argv[1]
except IndexError:
    print(f'Syntax Error - python3 main.py <domainname>')
    quit()

for i in records_types:
    try:
        answer = dns.resolver.resolve(domain, i)
        print('-'*30)
        for server in answer:
            print(f"{i} Records: {server.to_text()}")
    except dns.resolver.NoAnswer:
        pass
    except KeyboardInterrupt:
        quit()
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist')
        quit()
    except dns.resolver.LifetimeTimeout:
        pass
    except dns.resolver.NoNameservers:
        print('Please Provide a Valid URL')
        quit()
    except dns.name.LabelTooLong:
        print('URL too long')
        quit()

