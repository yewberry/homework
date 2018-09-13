# -*- coding: utf-8 -*-
import os
import base64
from wx.lib.embeddedimage import PyEmbeddedImage
# INSERT_START
logo48 = PyEmbeddedImage(
	b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QAAAAAAAD5Q7t/AAAA'
	b'CXBIWXMAAABIAAAASABGyWs+AAAACXZwQWcAAAAwAAAAMADO7oxXAAAOoklEQVRo3sWZe6xl'
	b'VX3HP2ut/TiPe899P+fF8JjyGF6OgAgtBRV8pRUrJlWrNG2tiYkx9q/W1iYmTVuqadqktoI2'
	b'lUiLEh9ELEasCFJE0BHKwIgww8xwZ4b7PPfe89qPtdavf+x979wpxjJzzbiTlXNy9tl7f7/r'
	b'+/391u+3tmKThznnGtyBx1T9nZ9sxEOT24O4un00ykYSVdGJpSlJ68XkhccPNR+8Y1WFMZKn'
	b'm33kSYc63Qvjy99BuvdrhO/9zPagb+Td1Wr1rVEYnKeVGqzTjnqqTwkq18gSNtvnWgt3t5+6'
	b'/yvx9Pnt+a//1S+NgDmdixqv/13Ofvwe/Ie+eEN9eOJzW0cH379zvH9nXyVsWGejLLemJ6FR'
	b'SoVa64YOwnNNtf+mcGRbZfWJrz4+eN2taXf/Q786AlO3/hOtf3/gkurQ+L+eNd64ZM/2QTU9'
	b'UCGxnmY7IcstqYQoQKtCZqV0qKLq5aY+ODN3z188pbQRRDZNQJ/y7F91C0c+9VtB0D/yx33V'
	b'+ILJRkxfHOC84J0jd4LRMFg1DFU0CHgRnAiiTS0Y3vqBys49U4PX/8EvRYHglAlccTOVsy7f'
	b'ocPoxmpkiIwmtZ5uZtk9LLxuxzSXbR9ipKp5/sUZbnu0STNVaCWFGpW+3dVzrrj4lgf+eeZ2'
	b'dfuZV6C261pM38j52gRbAqPIvWc1tbSSnMsmQj587RZ2jvXzveebPDWb0cpASgUKFcKGaYxd'
	b'drtSp2XfTSswdMM22vvCaa1UxQt0UkdqPZ3U8Y0DwveOHeB/ZpbIJaKTORJXpjoBUYLSShFU'
	b'poEQcGecwIcugj83wSRKqcx6VhOLVpBYz7EVSzdtU1UpmTKsJhYR8CUBpUArhTLhMBAByRkl'
	b'oLTh95VSWz/ypVEBerkjsZ5AKyqhZrw/pn+0Rl/UIJeApU7GQjtjuZvTzRzOFwFOEDeASJkA'
	b'cfbMELjgN25k/8OTDF81P5onrbNTgcQbdFRjYqDCaDVmaiBishEz1ajQqIYsdXNmmgmHF7sc'
	b'XOgys9SlmyREqEFdH6yo+ghu7sCmCLzqlXjk6t9G9ZYb0VmX/nU8OPHeuH9oIIpiKj6l7jtU'
	b'XJfIp0Q4KgbC0IAJsSYm0VVWpMqxNGK+6+m0Vzq6/fLdYfPQbQsP3fOzM6JA87kf43udtNFa'
	b'vvcv33LJVfOp23N8JcevLpK3llEiRNUqKq7ibIZLenhrCQUqUcxIpcJOY5jrWI4m1fpyZeyN'
	b'R1rtR4CDwGn76FUT8EszvGPPeelziy8/+rrhS48tqeqew9IgW1Gk7QiNohLHhIPDJL0OebeD'
	b'zXK89egoIqzXUVjS9goqzdl39Omf3LH3qe+xyUx0SkF8794XEJHu87PNH1zx2t1v3zE6rlye'
	b'Is4iXgjzHtWBYTrdhFwc4gRvPSiFNgqxXWzSQvsancf2zcFTi8Cm6olTIiAiyN47/D/+zV1P'
	b'XB0GrcGBegOprp2ELMXpCtpUiCoGrYqfi1zq8FmMywK8rbtO7g8D2WbAw2msxNkPn2WiUcsU'
	b'gnhfkBJBAIlrENdAq/XfAFBSVHUmBG1IkrT30kLzMJCfcQLRFeczPT40GQWm+gr1tYEwwATC'
	b'+rmiFAWtIQhAK6y1SS9J50TEn3EC7DiHVRWnCaa3sRwW50gXF0iOHUGSFCVSgi8JKA1KI3nO'
	b'UnN55dDs0ipPfmGz+E+9H4hml/jEnfc1t22fqv7aWdNXaa2LSRABEXRoUEqhjUHpDfOjNEpp'
	b'njnw0szff/nBOx54+uCDn/7Cf3Yyu7ly6JQV+Pid93F0pT3XSvOvZtYtqhK40gYVBCAOhS/A'
	b'K83GtVJEmF1uP33PD/ffBcy1k03H8GlYCHjPTVfzb9/8/s8Wlls/AQ/OItbhVYiEfYiKENGg'
	b'oyIuShIu7TA/v3AY2HT6XDtOuRoFuPuBHyIiiz/ef/A/xhq7r62Guu68wpsYbRQ68CijCvDO'
	b'gXh80iZbOELWas3xS0ifm1JARHj/jVfKJ27/6rdePDr7kCiNDgxaMpRPQDLwOZJ1cd1V0sXj'
	b'ZMcPYJst3+v4DmWF/StTAODObz8OMPfCoaNfn+4zb4riODRhBfEO6yxi86Ie6nRRNsEoj6hQ'
	b'66nzJ2Bv2L9lwraOvrhpAptq6+RHd/Lwkweic8cb7+wdP1TrzL9Eb2mOZHGWbKWJ73ZRTjBa'
	b'owONDqocu/jmc9LXvvnIs1+5Y3996y6fry5uisBpWWjtePjxA3TzwIX1Ad83MkloYpTzaDSB'
	b'CglNTBBEmDBEmxAdxTA2PT59yZV/u+XDn721k9TrvOGjZ16BCz7yGTo9H8zc8EeXDm+98M8u'
	b'CRZfUw+V0kphlCEIIoKwAG6CoJh9DasDO3hi9ErmetJ4csZen+3cs1VJfpTuyiKX3+w49MQp'
	b'Y3n1MfC+z8Nzj4Rm97XbDujRq6K3/8mNuj72hnx827YkmWeo2SKIKijnEGtRSqO1QaHQ2uOq'
	b'g+zb8uus6grHZ+fp5LpfN8b+0AyNvsWcfdl3VNa+301u/0H2wOeOMXGu49n7XxWsX9yR7b4F'
	b'9n1Lmd+7bTKa3H5d1N//NhPHr0ebbc5JePZYjSt3jXFpuMKNy48wuHgQ111FnEOXKy9BTG9o'
	b'C89MX8Pe+Gxebna456HneXnFYQJDWAmJqyFhHKSBlhdw6X+55flvdp5+9Inuvbc1iRuQrp4i'
	b'ges+Coef1eGbbz03Hp14d9zo/51KX+3CsBJGADZzZGmO8o492xpcuHWQ7WHGhdkRJrtHqdse'
	b'QRiSxg0WatMcqkxx3FWYX+1w/+OHePJIpyg3AkNUCYnrMZV6TFyLCUKDeN/O2+0ftY/N3N16'
	b'8uH78vv+7ij1Uegs/P8E9Ltuw88dC+vXvu2DlaGhj1UbtZ2VeqxMaEDA5g6bWWxucdYT4rlo'
	b'vMrF0w0mGxVGq4bhSFMNND0PzcQy30r46UyTh/bPcWA+RcrHKq0Io4CoGhFXI6JqRBAHGKMR'
	b'EbJuajvz83t7h5/7h/ThL35db9vd9Q9+9hcQGNjK+Jdeov2d+97e2L7tzvpQ31AQBqBAqaLG'
	b'd9bjrcM7j/eC94I4R8MI0zXNVD1gKDaESljpWY4s9Ti40OPYSkZW1m1S1k8iBYkgMARxQBiH'
	b'BFFAEBqUVsWEZTlJc6mdHHrmU/ZLf/opteuajjzznZ9PIPzAv5A354aHr37jlwe3jL8hjEO8'
	b'L4Aao1GAd0UTswZEfDGc8+S5xWYWl1lc7rDW4ZyUlSpISVq8x69dK4JCoUxBxIQBJtRorVFK'
	b'AYLNcrL5mXn7o6+9L37s7m8n6gTsk7JQ7cq3kb341G/G/X3XBKHBO0+aFk2TroQopVBaoVRB'
	b'Zp2AgA482mjCwOCiEJs7nC2Gtw7nPN4qlPN4B3jB48GX/Kwnd4LNXdlGeLQuShQBfFAbY3Tn'
	b'TYlSD6FNWtxkw0Km3vhRVj75njDsb9wcVeOKUooszUm7GXlaNO2oQnKtSyJaoY1GG1WQUwql'
	b'NcooTKAxgSEIy1kNDCYwRc0UmOI6rcsJKbwg3uOTFLe8iptdIJ9bIl9pY9McT4D0jV3D0NQE'
	b'5171SgWCi9+EmzxvR1itvD6MA5zzpL2MpJsSxQFQKeOAE42YbFRhw/An/nOiL1ZFX+xV2aEV'
	b'Y80mygtkOdJLkG4Xuh0kios9F22KlrQ6eC479pynPv6NI3KLOlmByjVvJRwYuTyoRFuVVtjM'
	b'knVS8m6K5IVc4qWMCX+S/zf6eSMZXwbqRnJsGEo8ynlUblFJCt0eqttD9XqoLAXrinLcuUKi'
	b'uD7EyPbL5Ba1jrv4EtVovUuhq32vMUEQiRNcN8W2evhOcSOXuyKFWo+zvghIKbPQejYqCbpi'
	b'yIbBhqGsQ2c5OsnR3QTd6aE7CTrJILMFcF9W3F7K7wqCiqY2dClQRQcbLHT+DTB/rKrC6CIR'
	b'sLnF9jL8chuyHNtXIe2lqCAo+10FgUYJJ7KKl1cCtw6xvphBWwBXuYPc/p9Rlh/OF/GAoCg3'
	b'BaQkLgI6hLh/F7WBYQYmOxx/rlBA7boOLrp+EB3s8M5jU4tPMlhtIastsm5KZzWh10lJ05w8'
	b's7jcF5nFlZ+2BG83gndgXWHB3EJmUZktLGNdAdhLuXGhwOh1v6u1HRcpFfC+OBf3TTG0ZYLr'
	b'P7jBQpO7YGBixKNHbV6sst45yBJ80iPtpnTbCUk3JUtzbFbYya8tavaEbbwrfhNbkilJYNdm'
	b'0hfBD4hSiNaIVojRiNYoo8EEqDULCSUBKeCG1T5qQyPc9bENFho9BxYOjzgv/Xlqy1XSg88h'
	b'z/Bphk8jMAZVpj9jHRi1HsjiPd7JSb4X50+cX9u9QyEbslCx/6hPymqEIQpBiSCqJLGW1nQU'
	b'Y+LhtfQVAFx000UsdfcNV8f64k4mdJO8CEjxYDOwOZSAfLlhaxXFgzfEwBpovwGwXwe+YSjW'
	b'SRQqKERKMhggLGyER9DrWasaGfrHh01vcqrS+umGdeDa18F37+2ZN53fSM4ZHYx+PNvj2eMt'
	b'5pZqLHdXsHlabJuUXnfaF/Hlyk+/YabXSfj1VVpOVBOc2HQ8oYSs7Y0pBVogKLYoa2FOdaqP'
	b'8akxLtg6yMWTNV54eS59YH9Dt8oQNwA/3R9x/J5PN5deOnw073VSo7wyodZGdchWF6STBkri'
	b'qiKKwZjioWXOX/d/GQ9uLaidnFzwieDX1gROjgG0RrQp7m00opFgdS4f61tOJrePdCcGzWLc'
	b'PHzwhce++/0ffPnzd7383/d9F5cvlmKedMTAMNXBrdHEzh1B/9CYc1LJpD4mE2fvYHTrNjUw'
	b'NmpqjQFdqdZVEEUoEwjKiEeJiJKNfl3z9MnZRMQ7XxZJOXmWkSdd0nZH0tVFusuztBeO6+PP'
	b'v6TtShMlq67VXJKV2TnEzgJLFG835ZXl9MmHLg2pKF6J9hfkBkYYmBxX/WMTqm94lEr/sET1'
	b'ftHRMGElIqyaogk2BnERIhnibdEFdS15r0ueNumttEk7C3SXmnSWFugsrJC0F4Am0AZ6FK+e'
	b'PMVbnJ+7k/e/zXCkdGagoA4AAAAldEVYdGNyZWF0ZS1kYXRlADIwMDktMDktMjhUMTE6Mjc6'
	b'NTYtMDQ6MDDdFKsUAAAAJXRFWHRtb2RpZnktZGF0ZQAyMDA5LTA5LTIzVDEwOjQxOjMyLTA0'
	b'OjAw0mO4iAAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAAASUVORK5C'
	b'YII='
)
zhao = PyEmbeddedImage(
	b'iVBORw0KGgoAAAANSUhEUgAAAEkAAAB6CAYAAADznX7fAAAEGWlDQ1BrQ0dDb2xvclNwYWNl'
	b'R2VuZXJpY1JHQgAAOI2NVV1oHFUUPrtzZyMkzlNsNIV0qD8NJQ2TVjShtLp/3d02bpZJNtoi'
	b'6GT27s6Yyc44M7v9oU9FUHwx6psUxL+3gCAo9Q/bPrQvlQol2tQgKD60+INQ6Ium65k7M5lp'
	b'urHeZe58853vnnvuuWfvBei5qliWkRQBFpquLRcy4nOHj4g9K5CEh6AXBqFXUR0rXalMAjZP'
	b'C3e1W99Dwntf2dXd/p+tt0YdFSBxH2Kz5qgLiI8B8KdVy3YBevqRHz/qWh72Yui3MUDEL3q4'
	b'4WPXw3M+fo1pZuQs4tOIBVVTaoiXEI/MxfhGDPsxsNZfoE1q66ro5aJim3XdoLFw72H+n23B'
	b'aIXzbcOnz5mfPoTvYVz7KzUl5+FRxEuqkp9G/Ajia219thzg25abkRE/BpDc3pqvphHvRFys'
	b'2weqvp+krbWKIX7nhDbzLOItiM8358pTwdirqpPFnMF2xLc1WvLyOwTAibpbmvHHcvttU57y'
	b'5+XqNZrLe3lE/Pq8eUj2fXKfOe3pfOjzhJYtB/yll5SDFcSDiH+hRkH25+L+sdxKEAMZahrl'
	b'SX8ukqMOWy/jXW2m6M9LDBc31B9LFuv6gVKg/0Szi3KAr1kGq1GMjU/aLbnq6/lRxc4XfJ98'
	b'hTargX++DbMJBSiYMIe9Ck1YAxFkKEAG3xbYaKmDDgYyFK0UGYpfoWYXG+fAPPI6tJnNwb7C'
	b'lP7IyF+D+bjOtCpkhz6CFrIa/I6sFtNl8auFXGMTP34sNwI/JhkgEtmDz14ySfaRcTIBInmK'
	b'PE32kxyyE2Tv+thKbEVePDfW/byMM1Kmm0XdObS7oGD/MypMXFPXrCwOtoYjyyn7BV29/MZf'
	b'sVzpLDdRtuIZnbpXzvlf+ev8MvYr/Gqk4H/kV/G3csdazLuyTMPsbFhzd1UabQbjFvDRmcWJ'
	b'xR3zcfHkVw9GfpbJmeev9F08WW8uDkaslwX6avlWGU6NRKz0g/SHtCy9J30o/ca9zX3Kfc19'
	b'zn3BXQKRO8ud477hLnAfc1/G9mrzGlrfexZ5GLdn6ZZrrEohI2wVHhZywjbhUWEy8icMCGNC'
	b'UdiBlq3r+xafL549HQ5jH+an+1y+LlYBifuxAvRN/lVVVOlwlCkdVm9NOL5BE4wkQ2SMlDZU'
	b'97hX86EilU/lUmkQUztTE6mx1EEPh7OmdqBtAvv8HdWpbrJS6tJj3n0CWdM6busNzRV3S9KT'
	b'YhqvNiqWmuroiKgYhshMjmhTh9ptWhsF7970j/SbMrsPE1suR5z7DMC+P/Hs+y7ijrQAlhyA'
	b'gccjbhjPygfeBTjzhNqy28EdkUh8C+DU9+z2v/oyeH791OncxHOs5y2AtTc7nb/f73TWPkD/'
	b'qwBnjX8BoJ98VQNcC+8AAAY7SURBVHgB7ZuLiiRJCEWnhv3/X94ZBwSxfFxDzXp0NjQZGaHX'
	b'6wmr6B3Yx/9/f37dPyGB3+HpffiPwA0JGIQb0g0JIACE3JN0QwIIACFfN0mPx+MX/U7+fBWk'
	b'aTgM+j9ebD+tBjb/jqV6U/prkCwo+iImG9Hak+/jHzdqHAE02URHC/E6Cgkp2GloKzfzPQYp'
	b'K2Q1OPWdYWkje6jnte+kyGQVjmymmhv5QM9WIU00JAGhTSFxFd2Rj5tVcAIQ0izHWB74rPsc'
	b'gXRiYrqpyqVUa18OiQyySX6eQL4y53JIVzZn1Tq5mK+BhDZvfSytPQl4BVJWVBqYWm/WXIGE'
	b'3uoUoG2dFUibt9oFcnKBK5C6jZzknzSP1hmH9KopQutacRngcUjo7bwyzgIV+flqSNmERGDk'
	b'2Tgkzxjte2fS0Duu2/8KYDVu7Z00P6VzUlvmjE+SFH/ndeV76XiSurecmezqVy+I61m+jiaJ'
	b'BatGON4ywmfR8zQv0kTOoEnqQiEj3Qaz/BOPpKnz6F3XciHpZIS4FaMLWjHvvvcEaQJOB8xE'
	b'/S50PU1H30ldExv5pxeD5JUhkaj8tRo+nQYvD2nE8oHmWXHSy9PHjRJkgCVgGZJ7JzmyZldL'
	b'5nfW5Il6eYJEoidNdsy8Qy73bF1W+eN2ZUNs/MqashbXfztIZIx/pWFkzU1RrFwjuRzDefyk'
	b'/RVI1siyCe9JpqQxL+6Kfe3D/E66wsh0DX0x+l03Xqm/MklkQJusmNqIJT/8W9V//CV8/D/g'
	b'ICAa8mEvSO1IoOLreJJQk2hc1JA+m9CsaBxBqhSgBqvxGop8f4VWGdKkSdn8q9ZIP/B3UiZm'
	b'fcazHAJj5VnAMi1EJ9KI8suTZDXg7UWFvZyTfbQOGqc9QJN0egOyWKRBcVEDUW6UJ+vLtaUX'
	b'6aSTZAnKgug6MkEaXh1vn+tm5xwnn5aXSMf9iztKooJZIeuc9zJt2RCyZj3WR3KsGNKxNNJJ'
	b'ssSsPTZqnek9y4iOOXnf8mBCyoohTSIaiI6GRTlRXlZX6+l3K/8JkhUkhSKDJ3Gcg+rKeC8n'
	b'64E10OcTpCjRMxXlZGek6ekizUa5Wb6Xqz3DkFBBXWDy3fPg7U/VTiGRgRMT2S1mDej8zIPn'
	b'U+tkdelc56SQENF3j9FNV/0+/Z2U3Vi1gI5nw1t1WJfrcH165zPeoyft6Vh5Tuu1SbIMyeKZ'
	b'MRk7tT6tuQbJakyb1O9WzukeXVJ2Uaj2pZBQU+8Wl0Ki2968cQuIVW/Cx+lkpZC4iQmTrJU9'
	b'o2YsgJle9zyE1DHUyc2aqmjzd1MEPqsXQuoIZ4W75wSqAqtTL4SkhSNo+ky/a63ovdJ8JTaq'
	b'GZ2FkK4wEJmTZxH0bZ8hJGkyW08a9YB4+5m37vkYpK4RNN8DRZc0eVHSzxqkjuEs1wMlG5tc'
	b'r0FCG8mAVJud1qP6a5CqzVXjo0uogEJiL4UUNSYhTcdJbWSt67uQEMJIwSxGG8ri9Xk3X+tZ'
	b'7y4kK9jbQ4GicV6dK/Yt6COQLOErGuIap/XRS4MhnRrhRug5oSH1OmsUENV4+jfuk8JoQTTu'
	b'xMPEBXga8CRFxj3xKIfPNsFxje4ThtRtppvfbVTmW16ii4YhySJ6bRXVMd57ZM7LuXof/k6q'
	b'NtMBZ0EgvaoHT8faj/ZGJikq8A1nHwVpejrpAmk6swl9KaTM3PQUnkKGIUUFqs0it3cFINT3'
	b'2hc3asCDQfnRxXh5G/vwJEXFr2rmFLzlr6IFQ7IKReDe5WzCN/xxi5re+mhUbtvyZwE60YQn'
	b'KRK3zFimP3UPhhQ1GAGM8jbPrIs79QlDsopyk9EZx1z5nPYDQ6o0eXpjlRperAeo42kFktfA'
	b'p+7/CEidKaKLbUPyxvtdpqYLqAwJBYLGTYPcqutOUucGOrnT4Cb00v8Ht3s7GpjW0+edpra0'
	b'3UnqmJW5bJyevJbnn7BOIdFNd287ghOdVQBO6Vg1U0hWUmWvC7hSS8ZO1oUhdSYqMhydyaZf'
	b'uS7/UwnSlDX6SN4rQUS1y5AiMT77ZCDcg3zCHzeZ9NPWXwHJ+nhPXuRXQJoEYml9PKTtKSJo'
	b'Hw/JuvnpvRsSQPSG9FMhTf+ddk/ST5yk6Skihl81SRuACNLKf7uR8FU/W2Ck/z9PtUktDiq7'
	b'MAAAAABJRU5ErkJggg=='
)
help32 = PyEmbeddedImage(
	b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QAAAAAAAD5Q7t/AAAA'
	b'CXBIWXMAAAUxAAAFMQG37ShSAAAACXZwQWcAAAAgAAAAIACH+pydAAAJ70lEQVRYw52Xa2xd'
	b'VXbHf3ufc8+574fvtX0T4yS2wZAEMuCAwiuDQkpSolGrESMxEgWkfigSahmNFKW0GiFGmpFQ'
	b'RfhiqarUfuFDB0qrkkzQBBLUQfGkM4E4hIfDTBxsB2f89vXj2udxz9l794PtxDUDQ7uk9eVI'
	b'e63/+q+z/2ttwTc3AVhAslqt5g8ePFjp6Ogol0ql9Pz8vDc8PDz7zjvvTI+Pjy8CIaCMMUYI'
	b'8UeDfpPE9qFDhzbt379/59133/3trVu37nIcp1kIkRNCuFrrUGtdj+N4emRk5KP+/v6+06dP'
	b'D7z99tsTQASY/y8A67777qs+++yz+/bs2fMX1Wr1HillQQhhaa3RWt8IJARCCIwxsVJqcWJi'
	b'4lx/f/+/vfLKK6cvXLgwBcT/VwDu4cOHdz399NM/aG9vP+g4TiWKIqIoIo5jtFYYbW4UJwRC'
	b'SCzLIpFIkEgkCMNw9tq1a794/fXX//Gll166ADS+VOFXgEr39vY+8uSTT/6kvb39kDFkPM8j'
	b'CHwaYUgjiqgtNRibCxibC1n0Y7TW2EKj4vg6SNu205VKZddtt912+y233DJ28uTJa6st+VoG'
	b'3KNHj+5/4okn/qFQKOwMgoAgCIiiBotexMB4yMVrPlPLBiEFthQ0Io2KG7RkBD1bs9zRliaf'
	b'skFIXNclmUyysLDw6bFjx/7uueeeO7WeiY0MWM8///zup5566qflcrnH9318zyMIG1wY9fmP'
	b'j5a5NCvI53O0lPO0lLI05VOUcmly2SQRFueH6/QPL5B2JC25BFrFaGPIZrMtbW1tnalU6uOz'
	b'Z89OAHojALFv377q4cOHf7Rly5Y/DcNQ+L6PHzb4r0GfU1ciMvkC26oFEhJkHJASEYWEwhER'
	b'KlYYISkVsizHgnODNTCGrZUURisA8vn85ra2tuT58+d/PT4+vrQRgPvCCy985/777/+BMSbl'
	b'eR5h2OD0oM8vRwybqmUymRSe32BHRfDnPVXu7a7wrW1N7NpWYtfWIgkUg+N1rEQSx3F4/8oc'
	b'Es3NLSm01liWJXK5XHulUrny5ptvXgLUdQCHDh1qf+aZZ/62WCze7nmeaIQhF8cCjv8uplAq'
	b'IW0HP9Ys1AN6bkpyZ0eJhCWxpMBJ2KRcm47WHF4Q0j+8gBI2IPloqEZ72WVzyUUpTTKZTGWz'
	b'Wffq1avvDQ4OLq4BkEeOHNnX09PzV0A2CAIWvIh//8RnnhyWm8SPNH5D4zUUvuchMbw3MMX7'
	b'g9OUcy6lrIsQAgn0fTbD9LJBGVgOFeO1Je69uYgtQUpJLpcrz83NnT19+vSwvdqbVHd3912p'
	b'VKrieR5Gx1yabPDZnCSZd5n3V0RHK4VWgg/GDe9fm8RvaHzfI4w0zz56K7YlsS1BGClmlxQS'
	b'iLXFxS+WuDiywAPdJaIoIplM5nfv3v0gcMYG2Lt3b1Nra+s9xhgZxxFBpPlkUrGgkzQigVZ6'
	b'RXiUJo41cSxRsUWsBCYSNBfTWHLlRl+dXmZwKqAe2xizAjr0Db/6bY0Hbm1CKQVgt7e3f6uz'
	b'szNnAzQ3N2fS6fRmpRRKrVD98WSEp7OEvkEpveKxIo5j4lgRx4ooCDjQ5fDw7S0IIZhfCnn1'
	b'zBcM1RTSMqAVWmlCX/PbiYAFP6aQtDDGYNt284MPPthsAyKTybipVKqgtcZoTawNs74hRCBi'
	b'g1YGHa+A0MqgDWituSmr+eGBDlqLKcJGzD+duszPP1kgIoFp3GhbpGCqHjG3FFFMWSilEELk'
	b'Ojo6yhLAdV3LdV0XwGAwBkIlviSUQgjWvhoV8727Sty5rYQxcObSJP/SN0EonNVjKzPCrI6K'
	b'oKEIInU9pJTSLRQKaQkQhmEchmGwps5CCJLWjSAbzRhD1lLs6SpiWxK/EfGzs6NMBhbSsv43'
	b'cLESJulIko51PaTWOpyfn/ckYDzPa3ieV18ZqWBJKLpg1o3b9RGNMWRdgdCKWj1gfM5nYCJE'
	b'WIk/hBaMopy1aco4aLPCpNa6PjIyMmsDTE1NLS0vL/++qanpdikl6YTkjmqCTwcbyI1BBVhS'
	b'sNAQ/Og/L+OaBpGRfFG3sCyBig0Cg1lHgkSzvZqmmLZRWiGEIIqi6b6+vmkJcO7cubmpqakP'
	b'hBDGsmxcW3Bn1SJDgF7VcSFACoNjQ8oVuMkETibLXbduoqW5QDaTIJuUpFxBwpZcX8WMIe/A'
	b'3u0VjDEIITHGxKOjox8PDw/XbYCZmRn/ypUrF3bu3DmdSCRawjBkZ9Xh7paQX4772G4SS4Kb'
	b'ECRtgSUErY7g7x/p4M4teea9iJ/8/DJ9Vz1iJVj2BUvLmmWliOIG396RZ3dnAa01jutijFns'
	b'7+8/AwRylSV9/PjxD2u12nnbtrFtm4wj+O7OFK32MioKcW3IpyCfEri2ZltRsn1TGjdh0VpI'
	b'0rMlg2sZcmmLYtYik7IQRrG1IHhqbxsZR4AQ2LbN5OTkB2fOnBkA1BoATpw4MXb27NmfRVE0'
	b'57ouUlrcsSnBX+5Okdd14ujGNiWF5ItZj4tDM2ituTa9yAdXZhDyRuN1FFF2Yn54cAv3dBaI'
	b'lcZxHKIomu3v7//Xd999dxww68exHhsbm3nooYc6KpXKTmOM0CpmS9GmkobPfl9nztNoI0BA'
	b'PdBc/HyKC5fHOd4/xkfTMRE2y17M3NwyRSvirx/exJ/tbgGtsG0b13XN6Ojom0ePHv3nzz//'
	b'fOFLG9HY2JjX1NR0rbu7e0ehUNiitUFoRVc5QXfZpl73GJ3xqC3FBLFgahk+HQ8YWQQvkiwu'
	b'eojQ5952l7/5kzYe3t4EWiEti2Qyyezs7K9fffXVH7/22muDf2gjAjB9fX3TXV1d411dXXdl'
	b'MpnmFdFQtOYke7al2d5sU3Y0oech4hALRd7WtKU1j3Rnefq+Ct/f08q2sru2hJBMJllaWhp4'
	b'6623fvziiy/+N+sW069ay5O9vb37H3300eebm5vvbzQaMggClFJIAZEGv6FRZkVnhABbQioh'
	b'SVgCpVfkznEcEomEnp2d/c2JEyd+euTIkfeMMd76RF+1lsuTJ09O12q1oc2bNxeampo2pdNp'
	b'17IslNYIwLEgaa1cy6QtcCyx+jiROI6D67rEcVwfGBh4p7e39+jLL798DvA36vtGBiwgDWRW'
	b'PV8ul296/PHHH3jsscce6ejouLlYLOaNMSil0FpjVqeNEALLWqlnYWFhcWhoaPDYsWOn3njj'
	b'jV/NzMyMAovA8qoHa0A2ApCAuw7Amheq1WrbgQMHbuvp6bllx44dN5fL5aZsNptKp9MJz/Oi'
	b'xcVFv1ar1S5dunT5ww8/HDx16tSliYmJMWB+XeL6Kgt/9B9Yewk7q+6uugNkOjs7i6VSKZ1O'
	b'p13HcWQURcrzvLBWq3lDQ0Nzq8nC1UpDVh4i8WrVX9uCb2Jig6/Z2uj8UpKvs/8BEIXflCnf'
	b'yHMAAAAldEVYdGNyZWF0ZS1kYXRlADIwMDktMTItMDhUMTM6MDI6NTktMDc6MDD8XINwAAAA'
	b'JXRFWHRkYXRlOmNyZWF0ZQAyMDEwLTAyLTIwVDIzOjI2OjIxLTA3OjAwfPt/cQAAACV0RVh0'
	b'ZGF0ZTptb2RpZnkAMjAxMC0wMS0xMVQwOTozMDoyOC0wNzowMNE7w64AAABndEVYdExpY2Vu'
	b'c2UAaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbGljZW5zZXMvYnktc2EvMy4wLyBvciBo'
	b'dHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9saWNlbnNlcy9MR1BMLzIuMS9bjzxjAAAAJXRF'
	b'WHRtb2RpZnktZGF0ZQAyMDA5LTEyLTA4VDEzOjAyOjU5LTA3OjAwo+31RAAAABl0RVh0U29m'
	b'dHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAATdEVYdFNvdXJjZQBPeHlnZW4gSWNvbnPs'
	b'GK7oAAAAJ3RFWHRTb3VyY2VfVVJMAGh0dHA6Ly93d3cub3h5Z2VuLWljb25zLm9yZy/vN6rL'
	b'AAAAAElFTkSuQmCC'
)
zhao32 = PyEmbeddedImage(
	b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAyElEQVR42u2XQRKAIAwD+f+n'
	b'16sHgSQtHhw740VAtjRtcYzfPOP2qHNbN+0AINr8buKHEd95AIZnMwD/+B+8TwAoA2w0gCBY'
	b'CwJDgIgASwhCxe+gKKTyduJqXFnbWng6105DUtENHV5TjO1yHDN1ZkWGVBtOiqmCKmeBWtEI'
	b'1qN6owLsjl2aSwCAEf/jAI4ISeOlaIBU1GlHIxS0BaAUoXJpRoRImxbJEVVvt+1F59jmUdU6'
	b'0Y4ZPW217cck/VgrwOu3oU8ASHYBKEtBzTEs854AAAAASUVORK5CYII='
)
flag_cn = PyEmbeddedImage(
	b'iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAIAAAD5gJpuAAAABGdBTUEAAK/INwWK6QAAABl0'
	b'RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAFqSURBVHjaYrzOwPAPjJgYQEDA'
	b'leHVbhADIvgHLPgHiQ0QQCxAlkR9NW8sw+cV/1gV/7Gb/hV4+vfzhj8Mv/78//Pn/+/f/8Ak'
	b'hH1t0yaAAAJp4I37zyz2lDfu79uqv/++/WYz+cuq/vvLxt8gdb+A5K9/v34B2SyyskBLAAII'
	b'5JAva/7/+/z367a/f3/8ZuT9+//Pr78vQUrB6n4CSSj6/RuoASCAWEDO/fD3ddEfhv9/OE3/'
	b'sKj8/n7k9/fDQNUIs/+DVf8HawAIIJCT/v38C3Hr95N/GDh/f94AVvT7N8RUBpjxQAVADQAB'
	b'BNLw/y/Ifwy/f/399ufTOpDBEPf8g5sN0QBEDAwAAQTWABEChgOSA9BVA00E2wAQQCANQBbE'
	b'if/AzoCqgLkbbBYwWP/+//sXqBYggFhAkfL7D7OkJFCOCSj65zfUeFjwg8z++/ffX5AGoGKA'
	b'AGI8jhSRyIw/SJH9D4aAYQoQYAA6rnMw1jU2vQAAAABJRU5ErkJggg=='
)
setting32 = PyEmbeddedImage(
	b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QAAAAAAAD5Q7t/AAAA'
	b'CXBIWXMAAA3XAAAN1wFCKJt4AAAACXZwQWcAAAAgAAAAIACH+pydAAAInElEQVRYw61Xe3BU'
	b'1Rn/nXMf+yJkwwbMi2QJ8ha3jtKoM1Ze0iDtTOsLEetoO3WmOsr4WGOjU8fpdOuyvCKijP3H'
	b'KpbacdoBra2DESwGofIwSrIJ2QQSyCYEEuLNPu69555z+kc2aTRgI/abuXPOnPud7/ud3/c4'
	b'90JKict9Xlj/O/pd9kspQXGZEo1Fbp42bVr/5roNb0djEeVr78hE7UwIQDQWWfby9pcaN25e'
	b'//TImsvl2rBq5Y/9paXTVwK4JacX2rRlQ19xccnZaCwSmIhtdSJKuq7X/fQnty/Ys+efV27Y'
	b'FAXn/E1d168qLJyKG6+/wXvmTNdT0Vgkoapq/c/W3hdoazth9vQkbwXwxv+FAUop87jduHv1'
	b'Pd6S4pLfKIpy8vbb7tSFECgqKsGCBVfdmJeX13THbXf5A4FC2A4TAKwxDE6+lG0ipRy3uO2V'
	b'F7cyxhYzxl4WQrzmcrn3rV1z7/f9fj8IobkEEshk0qBUgcfjBQA4DgOlFMcaj1n793+0VQjR'
	b'qGna83l5eRW2Zb/y8EOPPvI/QxCNRSYXFBT8avWda5QjRw9vbPz8s61TCqZwv9+PdDo1nLmU'
	b'Qggx6tQwBiGEgBACiqJi4YKrXX19fQ8LzsWiRVU+Sgn+/NafFk+Ygc11G9rvuXttZSBQCCEk'
	b'CAFs24Jt21BVDYqigFIFikIhJcC5A8YcMGbBNC14PG6oqg5KCVRVxQf1e7LN8aYnnnry169M'
	b'KAlt237uwMGG7bdW/8iXzWYgpQQhBG63B7ZtI9HeJk+fPp3u7DqlAkD59AqnrLTMFwzOIJMm'
	b'TYJhGODcgJTA1KlT0Rxv0qWUr13M1yiAXNncCsCilIYAQoQQkFJCUVTouo7WEy28/sMPTMFF'
	b'HRf8EIBGAGhpjYdOtLVWKYqy7gc3LXbPnjVbMQwDppmF43AEAgFuGMa+zXUbdCmkxhy2riZc'
	b'Wz8agmgsQvz+gp5geUWeBITb41GvCV3jppSCcwculxvvvLsr253sPmLb9pqacO2Zi50mGouU'
	b'aZq2s7io+Nofrljp6e8fgMulw+Px4vz5c6AKRTqVxscN//r80UceC40yUBOulZu2xOjMK2d5'
	b'ykrLiBACjNlwHAZN09Ecb+Ldye4jj6178qZvKtccsJs2bYntj7fEb5gRrFQuXBhAKpVCfr4f'
	b'nDvYt+/DjM3snaMlPjJhjN2ya/ffBtoSJxwhBDjnAIBUOoV9H+01bdtegwkKY2zNJwcbzEw2'
	b'A03TwBgDIPH++//IGEPGb598vOaFcQBqwrWNjuNc/+Heei6lBOcCAEF7IiGEEHWXov1STEgp'
	b'606d7BCEUBBCYFkWBo1BlxDizbG6NBc7JRqLVGua9uoVVxQLzjmEGGYg2ZtMCyEOTdT5iAgh'
	b'DvWd60urqgLbtsEYw7XXXCcVRTmxcfP6T6OxyM2jOaDr+lv5k/OrQ1eHvBUVM4htW+BcgBCC'
	b'3p4ebSTbv6U0njt/TqNUgRACg4ODKCoqVqtXrFJ7zyavO950/K/RWGSqGo1FqNvlXrJwYchX'
	b'Xh4EADjOfxkg9LJvbFBKQCkB5wKUEliWjZ7epDzVeTLjOGxvTbhW0JpwrTAt87aPG/Yffv2N'
	b'18zmeJNDCMD5cCKWlpZxAKHL8B8qKirhjDkQgkNRVBw++u9sc/z4vqEh4w7O+V2jIagJ134E'
	b'YFE0Fpl+8NAnJ0tLyqAoFI7joKy01JtInKgCsPvbnZ5WFRcVeUfC6TgMX345SDnnD9aEaxOj'
	b'emM3KYqy1uf1maqqwHE4LMtCsKKSqKq6LhqLlE3UeTQWKVMUdV0wWElSqTSE4LBthorpQUop'
	b'PRiNRULjAGzcvP5pt8v97OKbl/iGaRPIZDIAgBXLqz2apu2cKABVUXcuXbzMwx2OoSEDnA83'
	b'toKCgFY+PTiFUrpnRHf0Nty0JXZs7px538vP94MxhsJAISgdruFgMIj6vfVWa2vLp47DvrEV'
	b'q4q6c9as2YuWLlnuOnr0CGybwTQzSPYkM5xzR0hBM5n0kBCitCZcK0cBRGORZZqm1RFCGCRs'
	b'EBJavvQWl5QSHo8XwWAFOrs6xd/feydr23ZdrjeMlGeIEFql69q6ldWrPMGKGfT48S8wMHAB'
	b'Ugq0tDanTMvcLqX8FIALwHs14dr+rzDwtZN4CCFDy5euUAghueuYory8HF6vFx0d7bI7eSbb'
	b'2XVKAYCK6UFeXFLimVk5kxjGEFpbW2BZNqQUEEIi0d46lMlmHqoJ1+4YF66LUUkIuX/KlIAJ'
	b'wDf8pSMhpYO2tjbk5U3C5Mn5pKSkxLtk8TIAgGEYMAwD8XgLBgb6c/oSjuOAEILCwml5Z7q7'
	b'ngcwDsA4Bgghemxj9NjCBQvngxC0dyRSQggyf+4Cn9vtzhkXlxglRi6yeOtxm3Ou+Lw+q6Ag'
	b'4O1OnuYNHx8o273r3QEppT2OAUKIkouPns1mGxq/+GwOJJKnOju3Tc7Lm+92u1fPmTXPJaUA'
	b'5wJSCkiJUeeM2aBUgZQShvElLNNqe7Fu2y/uvueuVcXFqdWmae7fvetdCcBLCFEBmFJKMcoA'
	b'IUTPAXABcM2bPzcQb26xAbjuf+C+VVXXVz0zb858b7Knm58+0yXcLreYPXuei4Cg92wP7z2b'
	b'JKqissoZV7osy0J7R1vbs888dy+GP88tAPaYuZUDwMY2IgcAz41OvLnlQm7OdJdOhBCk71yf'
	b'7OzqTP/lrbd/2T8w0Np//pzknKP3bI94/Y87Hmjv6NjRfjJhZs3MCKM2ADZiZ8Q2AEtKyb4S'
	b'AimlAJAhhJhjmLAAaMeOfvZeZeWMR4eGjOyBhgMPHjl8NDF33pxX8/Pz13MhvI7jtDU3xb9o'
	b'boo3PhF+bIgxuzrR3v57AIM5xwyACSA74viSSfi1hCQY7paKb5JPT6fSFIACQPEX+LVw+PE/'
	b'KKp64+murp9ve2l7Q45BMYZJBkDkDndx+a6/19/1F/0//8dggoknMF4AAAAldEVYdGRhdGU6'
	b'Y3JlYXRlADIwMTAtMDItMTNUMjA6NTY6MzItMDc6MDBvGvNJAAAAJXRFWHRkYXRlOm1vZGlm'
	b'eQAyMDEwLTAxLTExVDA5OjE1OjIyLTA3OjAwyw7uZQAAADR0RVh0TGljZW5zZQBodHRwOi8v'
	b'Y3JlYXRpdmVjb21tb25zLm9yZy9saWNlbnNlcy9HUEwvMi4wL2xqBqgAAAAZdEVYdFNvZnR3'
	b'YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAE3RFWHRTb3VyY2UAR05PTUUtQ29sb3JzqplE'
	b'4gAAADF0RVh0U291cmNlX1VSTABodHRwOi8vY29kZS5nb29nbGUuY29tL3AvZ25vbWUtY29s'
	b'b3JzL1AdtesAAAAASUVORK5CYII='
)

# INSERT_END
def image2base64(path):
	icon = open(path, 'rb')
	iconData = icon.read()
	iconData = base64.b64encode(iconData)
	LIMIT = 72
	liIcon = []
	fn = os.path.basename(path).split('.')[0]
	liIcon.append('{} = PyEmbeddedImage('.format(fn))
	while True:
		sLimit = iconData[:LIMIT]
		iconData = iconData[LIMIT:]
		liIcon.append('\t%s' % sLimit)
		if len(sLimit) < LIMIT:
			break
	liIcon.append(")")
	return '\n'.join(liIcon)

def insert2file(str, res_path, startstr, endstr):
	fp = open(res_path)
	s = fp.read()
	fp.close()
	a = s.split('\n')
	idx_s = a.index(startstr)
	idx_e = a.index(endstr)
	s = '\n'.join(a[:idx_s+1]) + '\n'+str+'\n' + '\n'.join(a[idx_e:])
	fp = open(res_path, 'w')
	fp.write(s)
	fp.close()

if __name__ == '__main__':
	import sys
	import glob
	from os.path import isfile

	path = './res/*.png'
	files = [f for f in glob.glob(path) if isfile(f)]
	sb = ""
	for f in files:
		sb += image2base64(f) + '\n'
	res_file = sys.argv[0]
	insert2file(sb, res_file, "# INSERT_START", "# INSERT_END")





