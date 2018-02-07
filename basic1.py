import wx
import basic_form


class TestFrame (basic_form.basic_frame):
   def __init__(self, Parent, netlist):
      # Initialize parent class
      basic_form.basic_frame.__init__(self, Parent)

      # Now populate the netlist

      self.m_grid1.SetCellValue(0, 0, 'Test')
      print(netlist)
      for row in range (0, len(netlist)):
         if row < 30:
            #print (netlist [row])
            self.m_grid1.SetCellValue(row, 0, netlist[row][1])
            self.m_grid1.SetCellValue(row, 1, "1")


def load_netlist(filename):

   netlist = []

   with open(filename, 'r') as f:
      lines = f.readlines()

      for line in lines:
         row_data = []
         if line.find('(net ') > -1:
            # key words are code and name
            fields = line.split (' ')

            have_field = False
            for index in range (0, len(fields)):
               if fields [index] == '(code':
                  row_data.append(fields [index + 1][:-1])

               if fields [index] == '(name':
                  row_data.append(fields[index + 1].strip()[:-1])
                  have_field = True

            if have_field:
               netlist.append(row_data)

            #Now find the end of the net

      #print(netlist)

   return netlist

def main ():
   print ('Test basic wxWidget form')

   netlist = load_netlist('STM32_TestBoard1.net')
   app = wx.App(False)

   frame = TestFrame(None, netlist)

   #show the frame
   frame.Show(True)
   #start the applications
   app.MainLoop()


if __name__ == '__main__':
   main ()
