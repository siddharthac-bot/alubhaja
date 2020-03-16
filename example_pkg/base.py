def hello():
	return "Hello"

class salad():
    def __init__(self):
        self.path=''
        self.items=[]
        self.numbers=[]
    
    def write(self,path,salad,n_items):
        self.path=path
        #print(self.path)
        
        assert len(salad)==len(n_items),"not cool"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        for item,n_item in zip(salad,n_items):
            for k in range(0,n_item):
                filename=item+'{:0>2}'.format(k)+'.salad'
                #print(os.path.join(self.path,filename))
                f=open(os.path.join(self.path,filename),"w+")
                f.close()
                
    
    
    def read(self,path):
        flist=glob.glob(os.path.join(path,'*.salad'))
        a=[]
        for file in flist:
            pattern=r"(\w+)(\d\d).salad"
            a.append(re.findall(pattern,file))
            
            
        print(a)
        return(a)
            
       # return a
            
        
    
   