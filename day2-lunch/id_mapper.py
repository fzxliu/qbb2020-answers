# Updating into a function
import sys
def id_mapper(mapping_file, ctab_file, option):
    assert option == '1' or option == '2', 'option has to be 1 or 2'
    fly=open('fly.txt','r')
    q1_out=open(mapping_file, 'r')
    ctab_array=open(ctab_file, 'r')

    fh3=open('translated.txt',mode='w') 
    D1 ={}
    i=0
    for row in q1_out.readlines():
        D1[row.split( )[0]]=row.split( )[1]


    for row in ctab_array.readlines():
        fields=row.rstrip().split()
        if fields[0]=='t_id':
            fields[8]='uniprot_id'
            fh3.write('\t'.join(fields)+'\n')
        if fields[8] in D1:
            key=fields[8]
            fields[8]=D1[key]
            fh3.write('\t'.join(fields)+'\n')
        else:
            if option == '1':
                continue
            if option == '2':
                fields[8]='not found'
                fh3.write('\t'.join(fields)+'\n')

id_mapper(sys.argv[1], sys.argv[2], sys.argv[3])            