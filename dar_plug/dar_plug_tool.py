from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
from qgis.core import QgsRasterLayer


class VITool:
    def __init__(
        self, index_name, red_band, green_band,
         blue_band, output
    ):
        self.index = index_name
        self.red = red_band
        self.green = green_band
        self.blue = blue_band   
        self.output = output

    
    def calc_vari(self):
        r = QgsRasterCalculatorEntry()
        r.ref = self.red.name() + '@1'
        r.raster = self.red
        r.bandNumber = 1

        gr = QgsRasterCalculatorEntry()
        gr.ref = self.green.name() + '@2'
        gr.raster = self.green
        gr.bandNumber = 1

        b = QgsRasterCalculatorEntry()
        b.ref = self.blue.name() + '@3'
        b.raster = self.blue
        b.bandNumber = 1

        entries = list()
        entries.append(r)
        entries.append(gr)
        entries.append(b)

        expression =  '({0} - {1} ) / ({0} + {1} - {2})'.format(
            gr.ref, r.ref, b.ref
        )

        calc = QgsRasterCalculator(
            expression,
            self.output, "GTiff",
            self.red.extent(), self.red.width(), self.red.height(),
            entries
        )
        calc.processCalculation()
