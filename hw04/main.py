import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html='''
        <html>
        <body>
        '''
        for i in range(1,10):
            html+='<br>'
            for j in range(1,10):
                html+="%dx%d=%02d  " % (i,j,i*j)
            html+='</br>'    
        html+='''
        </body>
        </html>
        '''
        self.write(html)
class aaaMainHandler(tornado.web.RequestHandler):
    def get(self,n):
        n=int(n)
        html='''
        <html>
        <body>
        '''
        if (n)<10:
            for i in range(1,n+1):
                html+='<br>'
                for j in range(1,n+1):
                    html+="%dx%d=%02d  " % (i,j,i*j)
                html+='</br>'
        else:
            self.write("请出入一个n不超过9的正整数")    
        html+='''
        </body>
        </html>
        '''
        self.write(html)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/([0-9]+)", aaaMainHandler),],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

 
