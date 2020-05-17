#!/usr/bin/env python3
"""
Default proplot configuration settings and validators for
`rc_configurator` assignments.
"""
import numpy as np
import numbers
import cycler
from . import warnings
from matplotlib import rcParamsDefault as _rc_matplotlib_default_full

# Initial synced properties
COLOR = 'black'
CMAP = 'fire'
CYCLE = 'colorblind'
CYCLIC = 'twilight'
DIVERGING = 'div'
FRAMEALPHA = 0.8  # legend and colorbar
GRIDALPHA = 0.1
GRIDBELOW = 'line'
GRIDCOLOR = 'black'
GRIDRATIO = 0.5  # differentiated from major by half size reduction
GRIDSTYLE = '-'
LARGE = 10.0
LINEWIDTH = 0.8
MARGIN = 0.05
SMALL = 9.0
TICKDIR = 'out'
TICKLEN = 2.0
TICKLENRATIO = 0.5  # differentiated from major by half length reduction
TICKMINOR = True
TICKPAD = 2.0
TICKRATIO = 0.8  # very slight width reduction

# Deprecated settings
# TODO: Add 'openrgb' setting for renaming shorthand color names to
_rc_removed = {  # {key: version} dictionary
    'rgbcycle': '0.6',
    'tick.labelpad': '0.6',
}
_rc_renamed = {  # {old_key: (new_key, version)} dictionary
    'align': ('subplots.align', '0.6'),
    'axes.facealpha': ('axes.alpha', '0.6'),
    'geoaxes.edgecolor': ('axes.edgecolor', '0.6'),
    'geoaxes.facealpha': ('axes.alpha', '0.6'),
    'geoaxes.facecolor': ('axes.facecolor', '0.6'),
    'geoaxes.linewidth': ('axes.linewidth', '0.6'),
    'geogrid.alpha': ('grid.alpha', '0.6'),
    'geogrid.color': ('grid.color', '0.6'),
    'geogrid.linewidth': ('grid.linewidth', '0.6'),
    'geogrid.linestyle': ('grid.linestyle', '0.6'),
    'geogrid.color': ('grid.color', '0.6'),
    'geogrid.labelpad': ('grid.labelpad', '0.6'),
    'geogrid.labels': ('grid.labels', '0.6'),
    'geogrid.labelsize': ('grid.labelsize', '0.6'),
    'geogrid.latmax': ('grid.latmax', '0.6'),
    'geogrid.latstep': ('grid.latstep', '0.6'),
    'geogrid.linestyle': ('grid.linestyle', '0.6'),
    'geogrid.linewidth': ('grid.linewidth', '0.6'),
    'geogrid.lonstep': ('grid.lonstep', '0.6'),
    'geogrid.rotatelabels': ('grid.rotatelabels', '0.6'),
    'share': ('subplots.share', '0.6'),
    'small': ('font.small', '0.6'),
    'large': ('font.large', '0.6'),
    'span': ('subplots.span', '0.6'),
    'tight': ('subplots.tight', '0.6'),
}

# ProPlot overrides of matplotlib default style
# WARNING: Critical to include every parameter here that can be changed by a
# "meta" setting so that _get_default_param returns the value imposed by *proplot*
# and so that "changed" settings detectd by rc_configurator.save are correct.
# NOTE: Hard to say what best value for 'margin' is. 0 is bad for bar plots and scatter
# plots, 0.05 is good for line plot in y direction but not x direction.
_rc_matplotlib_default = {
    'axes.axisbelow': GRIDBELOW,
    'axes.grid': True,  # enable lightweight transparent grid by default
    'axes.grid.which': 'major',
    'axes.labelpad': 3.0,  # more compact
    'axes.labelsize': SMALL,
    'axes.titlesize': LARGE,
    'axes.titlepad': 3.0,  # more compact
    'axes.titleweight': 'normal',
    'axes.xmargin': MARGIN,
    'axes.ymargin': MARGIN,
    'figure.autolayout': False,
    'figure.dpi': 100,
    'figure.facecolor': '#f2f2f2',  # similar to MATLAB interface
    'figure.titlesize': LARGE,
    'figure.titleweight': 'bold',  # differentiate from axes titles
    'font.serif': [  # NOTE: font lists passed to rcParams are lists, not tuples
        'TeX Gyre Schola',  # Century lookalike
        'TeX Gyre Bonum',  # Bookman lookalike
        'TeX Gyre Termes',  # Times New Roman lookalike
        'TeX Gyre Pagella',  # Palatino lookalike
        'DejaVu Serif',
        'Bitstream Vera Serif',
        'Computer Modern Roman',
        'Bookman',
        'Century Schoolbook L',
        'Charter',
        'ITC Bookman',
        'New Century Schoolbook',
        'Nimbus Roman No9 L',
        'Palatino',
        'Times New Roman',
        'Times',
        'Utopia',
        'serif'
    ],
    'font.sans-serif': [
        'TeX Gyre Heros',  # Helvetica lookalike
        'DejaVu Sans',
        'Bitstream Vera Sans',
        'Computer Modern Sans Serif',
        'Arial',
        'Avenir',
        'Fira Math',
        'Frutiger',
        'Geneva',
        'Gill Sans',
        'Helvetica',
        'Lucid',
        'Lucida Grande',
        'Myriad Pro',
        'Noto Sans',
        'Roboto',
        'Source Sans Pro',
        'Tahoma',
        'Trebuchet MS',
        'Ubuntu',
        'Univers',
        'Verdana',
        'sans-serif'
    ],
    'font.monospace': [
        'TeX Gyre Cursor',  # Courier lookalike
        'DejaVu Sans Mono',
        'Bitstream Vera Sans Mono',
        'Computer Modern Typewriter',
        'Andale Mono',
        'Courier New',
        'Courier',
        'Fixed',
        'Nimbus Mono L',
        'Terminal',
        'monospace'
    ],
    'font.cursive': [
        'TeX Gyre Chorus',  # Chancery lookalike
        'Apple Chancery',
        'Felipa',
        'Sand',
        'Script MT',
        'Textile',
        'Zapf Chancery',
        'cursive'
    ],
    'font.fantasy': [
        'TeX Gyre Adventor',  # Avant Garde lookalike
        'Avant Garde',
        'Charcoal',
        'Chicago',
        'Comic Sans MS',
        'Futura',
        'Humor Sans',
        'Impact',
        'Optima',
        'Western',
        'xkcd',
        'fantasy'
    ],
    'font.size': SMALL,
    'grid.alpha': GRIDALPHA,  # lightweight unobtrusive gridlines
    'grid.color': GRIDCOLOR,  # lightweight unobtrusive gridlines
    'grid.linestyle': GRIDSTYLE,
    'grid.linewidth': LINEWIDTH,
    'hatch.color': COLOR,
    'hatch.linewidth': LINEWIDTH,
    'image.cmap': CMAP,
    'lines.linestyle': '-',
    'lines.linewidth': 1.5,
    'lines.markersize': 6.0,
    'legend.borderaxespad': 0,  # looks sleeker flush against edge
    'legend.borderpad': 0.5,  # a bit more space
    'legend.columnspacing': 1.5,  # more compact
    'legend.fancybox': False,  # looks modern without curvy box
    'legend.fontsize': SMALL,
    'legend.framealpha': FRAMEALPHA,
    'legend.handletextpad': 0.5,
    'mathtext.fontset': 'custom',
    'mathtext.default': 'regular',
    'savefig.bbox': None,  # use custom tight layout
    'savefig.directory': '',  # current directory
    'savefig.dpi': 300,  # low dpi to improve performance, high dpi when it matters
    'savefig.facecolor': 'white',  # different from figure.facecolor
    'savefig.format': 'pdf',  # most users use bitmap, but vector graphics are better
    'savefig.transparent': True,
    'xtick.direction': TICKDIR,
    'xtick.labelsize': SMALL,
    'xtick.major.pad': TICKPAD,
    'xtick.major.size': TICKLEN,
    'xtick.major.width': LINEWIDTH,
    'xtick.minor.pad': TICKPAD,
    'xtick.minor.size': TICKLEN * TICKLENRATIO,
    'xtick.minor.visible': TICKMINOR,
    'xtick.minor.width': LINEWIDTH * TICKRATIO,
    'ytick.direction': TICKDIR,
    'ytick.labelsize': SMALL,
    'ytick.major.pad': TICKPAD,
    'ytick.major.size': TICKLEN,
    'ytick.major.width': LINEWIDTH,
    'ytick.minor.pad': TICKPAD,
    'ytick.minor.size': TICKLEN * TICKLENRATIO,
    'ytick.minor.width': LINEWIDTH * TICKRATIO,
    'ytick.minor.visible': TICKMINOR,
}

# Proplot pseudo-settings
# TODO: More consistent behavior for how format() handles rc params. Currently
# some things are only keyword arguments while others are actual settings, but not
# obvious which is which. For example xticklen and yticklen should be quick settings.
# TODO: Implement these as bonafide matplotlib settings by subclassing
# matplotlib's RcParams and adding new validators. Quick settings should
# be implemented under __getitem__.
_addendum_units = ' Units are interpted by `~proplot.utils.units`.'
_addendum_fonts = (
    ' See `this page ',
    '<https://matplotlib.org/3.1.1/tutorials/text/text_props.html#default-font>`__ '
    'for a list of valid relative font sizes.'
)
_rc_proplot = {
    # Stylesheet
    'style': (
        None,
        'The default matplotlib `stylesheet '
        '<https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`__ '  # noqa: E501
        'name. If ``None``, a custom proplot style is used. '
        "If ``'default'``, the default matplotlib style is used."
    ),

    # A-b-c labels
    'abc': (
        False,
        'Boolean, whether to draw a-b-c labels by default.'
    ),
    'abc.border': (
        True,
        'Boolean, indicates whether to draw a white border around a-b-c labels '
        'when :rcraw:`abc.loc` is inside the axes.'
    ),
    'abc.borderwidth': (
        1.5,
        'Width of the white border around a-b-c labels.'
    ),
    'abc.color': (
        'black',
        'a-b-c label color.'
    ),
    'abc.loc': (
        'l',  # left side above the axes
        'a-b-c label position. For options, see `~proplot.axes.Axes.format`.',
    ),
    'abc.size': (
        LARGE,
        'a-b-c label font size.'
    ),
    'abc.style': (
        'a',
        'a-b-c label style. For options, see `~proplot.axes.Axes.format`.'
    ),
    'abc.weight': (
        'bold',
        'a-b-c label font weight.'
    ),

    # Axes additions
    'alpha': (
        1,
        'The opacity of the background axes patch.'
    ),
    'axes.alpha': (
        1.0,
        'Opacity of the background axes patch.'
    ),
    'axes.formatter.timerotation': (
        90,
        'Float, indicates the default *x* axis tick label rotation '
        'for datetime tick labels.'
    ),
    'axes.formatter.zerotrim': (
        True,
        'Boolean, indicates whether trailing decimal zeros are trimmed on tick labels.'
    ),

    # Country borders
    'borders': (
        False,
        'Boolean, toggles country border lines on and off.'
    ),
    'borders.color': (
        'black',
        'Line color for country borders.'
    ),
    'borders.linewidth': (
        LINEWIDTH,
        'Line width for country borders.'
    ),

    # Bottom subplot labels
    'bottomlabel.color': (
        'black',
        'Font color for column labels on the bottom of the figure.'
    ),
    'bottomlabel.size': (
        LARGE,
        'Font size for column labels on the bottom of the figure.'
    ),
    'bottomlabel.weight': (
        'bold',
        'Font weight for column labels on the bottom of the figure.'
    ),

    # Coastlines
    'coast': (
        False,
        'Boolean, toggles coastline lines on and off.'
    ),
    'coast.color': (
        'black',
        'Line color for coast lines.'
    ),
    'coast.linewidth': (
        LINEWIDTH,
        'Line width for coast lines.'
    ),

    # Colorbars
    'colorbar.extend': (
        '1.3em',
        'Length of rectangular or triangular "extensions" for panel colorbars. '
        + _addendum_units
    ),
    'colorbar.framealpha': (
        FRAMEALPHA,
        'Opacity for inset colorbar frames.'
    ),
    'colorbar.frameon': (
        True,
        'Boolean, indicates whether to draw a frame behind inset colorbars.'
    ),
    'colorbar.grid': (
        False,
        'Boolean, indicates whether to draw borders between each level of the colorbar.'
    ),
    'colorbar.insetextend': (
        '1em',
        'Length of rectangular or triangular "extensions" for inset colorbars. '
        + _addendum_units
    ),
    'colorbar.insetlength': (
        '8em',
        'Length of inset colorbars. ' + _addendum_units
    ),
    'colorbar.insetpad': (
        '0.5em',
        'Padding between axes edge and inset colorbars.'
    ),
    'colorbar.insetwidth': (
        '1.2em',
        'Width of inset colorbars. ' + _addendum_units
    ),
    'colorbar.length': (
        1,
        'Length of outer colorbars.'
    ),
    'colorbar.loc': (
        'right',
        'Inset colorbar location, options are listed in `~proplot.axes.Axes.colorbar`.'
    ),
    'colorbar.width': (
        '1.5em',
        'Width of outer colorbars. ' + _addendum_units
    ),

    # Style shorthands
    'cmap': (
        CMAP,
        'The default sequential colormap.'
    ),
    'color': (
        COLOR,
        'The color of axis spines, tick marks, tick labels, and labels.'
    ),
    'cycle': (
        CYCLE,
        'The name of the color cycle used for plot elements like lines.',
    ),
    'facecolor': (
        'white',
        'The color of the background axes patch.'
    ),

    # Font setting
    'font.name': (
        'sans-serif',
        "Alias for :rcraw:`font.family`. The default is ``'sans-serif'``."
    ),
    'font.small': (
        'medium',
        'Meta setting that changes '
        ':rcraw:`tick.labelsize`, :rcraw:`axes.labelsize`, :rcraw:`legend.fontsize`,'
        "and :rcraw:`grid.labelsize` simultaneously. Default is ``'medium'``, i.e. "
        'the value of :rcraw:`font.size`.' + _addendum_fonts
    ),
    'font.large': (
        'med-large',
        'Meta setting that changes '
        ':rcraw:`abc.size`, :rcraw:`title.size`, :rcraw:`suptitle.size`, '
        'and subplot label settings like :rcraw:`leftlabel.size` simultaneously. '
        "Default is ``'med-large'``, i.e. 1.1. times :rcraw:`font.size`."
        + _addendum_fonts
    ),

    # Gridlines
    'grid': (
        True,
        'Boolean, toggles major grid lines on and off.'
    ),
    'grid.below': (
        GRIDBELOW,  # like axes.axisbelow
        'Alias for :rcraw:`axes.axisbelow`. If ``False``, draw gridlines on top of '
        "everything. If ``True``, underneath everything. If ``'line'``, "
        'underneath patches only.'
    ),
    'grid.labelpad': (
        5,  # use cartopy default
        'Padding in points between map boundary edge and meridian and '
        'parallel labels for `~proplot.axes.GeoAxes`.'
    ),
    'grid.labels': (
        False,
        'Boolean, indicates whether to label the meridians and parallels '
        'for `~proplot.axes.GeoAxes`.'
    ),
    'grid.labelrotate': (
        True,  # False limits projections where labels are available
        'Whether to rotate meridian and parallel `~proplot.axes.CartopyAxes` '
        'gridline labels.'
    ),
    'grid.labelsize': (
        SMALL,
        'Font size for meridian and parallel labels for `~proplot.axes.GeoAxes`. '
        'Inherits from :rcraw:`small`.'
    ),
    'grid.latmax': (
        90,
        'Latitude poleward of which meridian gridlines are cut off for '
        '`~proplot.axes.GeoAxes`. This works always for all basemap projections '
        'but only some cartopy projections.'
    ),
    'grid.latstep': (
        20,
        'Interval for `~proplot.axes.GeoAxes` parallel gridlines in degrees.'
    ),
    'grid.latinline': (
        False,
        'Whether to use inline labels for `~proplot.axes.CartopyAxes` '
        'parallel gridlines.'
    ),
    'grid.lonstep': (
        30,
        'Interval for `~proplot.axes.GeoAxes` meridian gridlines in degrees.'
    ),
    'grid.loninline': (
        False,
        'Whether to use inline labels for `~proplot.axes.CartopyAxes` '
        'meridian gridlines.'
    ),
    'grid.ratio': (
        GRIDRATIO,
        'Ratio of minor gridline width to major gridline width.'
    ),

    # Minor gridlines
    'gridminor': (
        False,
        'Boolean, toggles minor grid lines on and off.'
    ),
    'gridminor.alpha': (
        GRIDALPHA,
        'Minor gridline transparency.'
    ),
    'gridminor.color': (
        GRIDCOLOR,
        'Minor gridline color.'
    ),
    'gridminor.latstep': (
        5,
        'Interval for parallel gridlines in degrees.'
    ),
    'gridminor.linestyle': (
        GRIDSTYLE,
        'Minor gridline style.'
    ),
    'gridminor.linewidth': (
        GRIDRATIO * LINEWIDTH,
        'Minor gridline width.'
    ),
    'gridminor.lonstep': (
        10,
        'Interval for meridian gridlines in degrees.'
    ),

    # Image additions
    'image.edgefix': (
        True,
        'Whether to fix the `white-lines-between-filled-contours '
        '<https://stackoverflow.com/q/8263769/4970632>`__ and '
        '`white-lines-between-pcolor-rectangles '
        '<https://stackoverflow.com/q/27092991/4970632>`__ issues. '
        'This slows down figure rendering a bit.'
    ),
    'image.levels': (
        11,
        'Default number of levels for ``pcolormesh`` and ``contourf`` plots.'
    ),

    # Backend stuff
    'inlinefmt': (
        'retina',
        'The inline backend figure format or list thereof. Valid formats include '
        "``'svg'``, ``'pdf'``, ``'retina'``, ``'png'``, and ``jpeg``."
    ),

    # Inner borders
    'innerborders': (
        False,
        'Boolean, toggles internal border lines on and off, e.g. '
        'for states and provinces.'
    ),
    'innerborders.color': (
        'black',
        'Line color for internal border lines.'
    ),
    'innerborders.linewidth': (
        LINEWIDTH,
        'Line width for internal border lines.'
    ),

    # Lake patches
    'lakes': (
        False,
        'Boolean, toggles lake patches on and off.'
    ),
    'lakes.color': (
        'w',
        'Face color for lake patches.'
    ),

    # Land patches
    'land': (
        False,
        'Boolean, toggles patches on and off.'
    ),
    'land.color': (
        'black',
        'Face color for land patches.'
    ),

    # Left subplot labels
    'leftlabel.color': (
        'black',
        'Font color for row labels on the left-hand side.'
    ),
    'leftlabel.size': (
        LARGE,
        'Font size for row labels on the left-hand side.'
    ),
    'leftlabel.weight': (
        'bold',
        'Font weight for row labels on the left-hand side.'
    ),

    # Edge width bulk setting
    'linewidth': (
        LINEWIDTH,
        'Thickness of axes spines and major tick lines.'
    ),

    # Misc bulk settings
    'lut': (
        256,
        'The number of colors to put in the colormap lookup table.'
    ),
    'margin': (
        MARGIN,
        'The margin of space between axes edges and objects plotted inside the axes '
        'if ``xlim`` and ``ylim`` are unset.'
    ),

    # For negative positive patches
    'negcolor': (
        'blue7',
        'The color for negative bars and shaded areas when using ``negpos=True``. '
        'See also :rcraw:`poscolor`.'
    ),
    'poscolor': (
        'red7',
        'The color for positive bars and shaded areas when using ``negpos=True``. '
        'See also :rcraw:`negcolor`.'
    ),

    # Ocean patches
    'ocean': (
        False,
        'Boolean, toggles ocean patches on and off.'
    ),
    'ocean.color': (
        'w',
        'Face color for ocean patches.'
    ),

    # Geographic resolution
    'reso': (
        'med',
        'Resolution for `~proplot.axes.GeoAxes` geographic features. '
        "Must be one of ``'lo'``, ``'med'``, or ``'hi'``."
    ),

    # Right subplot labels
    'rightlabel.color': (
        'black',
        'Font color for row labels on the right-hand side.'
    ),
    'rightlabel.size': (
        LARGE,
        'Font size for row labels on the right-hand side.'
    ),
    'rightlabel.weight': (
        'bold',
        'Font weight for row labels on the right-hand side.'
    ),

    # River lines
    'rivers': (
        False,
        'Boolean, toggles river lines on and off.'
    ),
    'rivers.color': (
        'black',
        'Line color for river lines.'
    ),
    'rivers.linewidth': (
        LINEWIDTH,
        'Line width for river lines.'
    ),

    # Subplots settings
    'subplots.align': (
        False,
        'Whether to align axis labels during draw. See `aligning labels '
        '<https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/align_labels_demo.html>`__.'  # noqa: E501
    ),
    'subplots.axpad': (
        '1em',
        'Padding between adjacent subplots. ' + _addendum_units
    ),
    'subplots.axwidth': (
        '18em',
        'Default width of each axes. ' + _addendum_units
    ),
    'subplots.pad': (
        '0.5em',
        'Padding around figure edge. ' + _addendum_units
    ),
    'subplots.panelpad': (
        '0.5em',
        'Padding between subplots and panels, and between stacked panels. '
        + _addendum_units
    ),
    'subplots.panelwidth': (
        '4em',
        'Width of side panels. ' + _addendum_units
    ),
    'subplots.share': (
        3,
        'The axis sharing level, one of ``0``, ``1``, ``2``, or ``3``. '
        'See :ref:`the user guide <ug_share>` for details.'
        'See `~proplot.ui.subplots` for details.'
    ),
    'subplots.span': (
        True,
        'Boolean, toggles spanning axis labels. See `~proplot.ui.subplots` for details.'
    ),
    'subplots.tight': (
        True,
        'Boolean, indicates whether to auto-adjust figure bounds and subplot spacings.'
    ),

    # Super title settings
    'suptitle.color': (
        'black',
        'Figure title color.'
    ),
    'suptitle.size': (
        LARGE,
        'Figure title font size.'
    ),
    'suptitle.weight': (
        'bold',
        'Figure title font weight.'
    ),

    # Tick settings
    'tick.color': (
        COLOR,
        'Major and minor tick color.'
    ),
    'tick.dir': (
        TICKDIR,
        'Major and minor tick direction. Must be one of '
        "'``'out'``, ``'in'``, or ``'inout'``."
    ),
    'tick.labelcolor': (
        COLOR,
        'Axis tick label color. Mirrors the *axis* label '
        ':rcraw:`axes.labelcolor` setting.'
    ),
    'tick.labelsize': (
        SMALL,
        'Axis tick label font size. Mirrors the *axis* label '
        ':rcraw:`axes.labelsize` setting.'
    ),
    'tick.labelweight': (
        'normal',
        'Axis tick label font weight. Mirrors the *axis* label '
        ':rcraw:`axes.labelweight` setting.'
    ),
    'tick.len': (
        TICKLEN,
        'Length of major ticks in points.'
    ),
    'tick.lenratio': (
        TICKLENRATIO,
        'Ratio of minor tickline length to major tickline length.'
    ),
    'tick.minor': (
        TICKMINOR,
        'Boolean, toggles minor ticks on and off.',
    ),
    'tick.pad': (
        TICKPAD,
        'Padding between ticks and tick labels in points.'
    ),
    'tick.ratio': (
        TICKRATIO,
        'Ratio of minor tickline width to major tickline width.'
    ),

    # Title settings
    'title.border': (
        True,
        'Boolean, indicates whether to draw a white border around titles '
        'when :rcraw:`title.loc` is inside the axes.'
    ),
    'title.borderwidth': (
        1.5,
        'Width of the white border around titles.'
    ),
    'title.color': (
        'black',
        'Axes title color.'
    ),
    'title.loc': (
        'c',
        'Title position. For options, see `~proplot.axes.Axes.format`.'
    ),
    'title.pad': (
        3.0,
        'Padding between the axes and in arbitrary units. '
        'Alias for :rcraw:`axes.titlepad`.'
    ),
    'title.size': (
        LARGE,
        'Axes title font size.'
    ),
    'title.weight': (
        'normal',
        'Axes title font weight.'
    ),

    # Top subplot label settings
    'toplabel.color': (
        'black',
        'Font color for column labels on the top of the figure.'
    ),
    'toplabel.size': (
        LARGE,
        'Font size for column labels on the top of the figure.'
    ),
    'toplabel.weight': (
        'bold',
        'Font weight for column labels on the top of the figure.'
    ),
}

# Child settings -- changing the parent changes all the children, but changing
# any of the children does not change the parent.
# NOTE: Do not link title.color to axes.titlecolor because the latter
# can have value 'auto' which is not handled in format() right now,
# and because setting was only introduced in version 3.2.
_rc_children = {
    'color': (  # change the 'color' of an axes
        'axes.edgecolor', 'axes.labelcolor',
        'tick.labelcolor', 'hatch.color', 'xtick.color', 'ytick.color'
    ),
    'font.small': (  # the 'small' fonts
        'tick.labelsize', 'xtick.labelsize', 'ytick.labelsize',
        'axes.labelsize', 'legend.fontsize', 'grid.labelsize'
    ),
    'font.large': (  # the 'large' fonts
        'abc.size', 'figure.titlesize',
        'axes.titlesize', 'suptitle.size', 'title.size',
        'leftlabel.size', 'toplabel.size',
        'rightlabel.size', 'bottomlabel.size'
    ),
    'linewidth': (  # also sets minor tick widths through tick.ratio
        'axes.linewidth', 'hatch.linewidth',
        'xtick.major.width', 'ytick.major.width'
    ),
    'margin': (
        'axes.xmargin', 'axes.ymargin'
    ),
    'tick.color': (
        'xtick.color', 'ytick.color',
    ),
    'tick.dir': (
        'xtick.direction', 'ytick.direction'
    ),
    'tick.len': (
        'xtick.major.size', 'ytick.major.size'
    ),
    'tick.labelsize': (
        'xtick.labelsize', 'ytick.labelsize',
    ),
    'tick.pad': (
        'xtick.major.pad', 'xtick.minor.pad',
        'ytick.major.pad', 'ytick.minor.pad'
    ),
    'grid.color': (
        'gridminor.color',
    ),
    'grid.linewidth': (
        'gridminor.linewidth',
    ),
    'grid.linestyle': (
        'gridminor.linestyle',
    ),
    'grid.alpha': (
        'gridminor.alpha',
    ),
}

# Symmetric aliases. Changing one setting changes the other
_rc_aliases = {
    'alpha': 'axes.alpha',
    'axes.titlesize': 'title.size',  # NOTE: translate "auto" to color
    'facecolor': 'axes.facecolor',
    'font.name': 'font.family',
    'grid.below': 'axes.axisbelow',
    'title.pad': 'axes.titlepad',
}
for key, value in _rc_aliases.items():
    _rc_children[key] = (value,)
    _rc_children[value] = (key,)

# Various helper dicts
_rc_proplot_default = {
    key: value for key, (value, *_) in _rc_proplot.items()
}

_rc_nodots = {
    name.replace('.', ''): name
    for dict_ in (_rc_proplot_default, _rc_matplotlib_default_full)
    for name in dict_.keys()
}

_rc_categories = {
    '.'.join(name.split('.')[:i + 1])
    for dict_ in (_rc_proplot_default, _rc_matplotlib_default_full)
    for name in dict_
    for i in range(len(name.split('.')) - 1)
}


def _get_default_param(key):
    """
    Get the default parameter from one of three places. This is
    used for the :rc: role when compiling docs.
    """
    sentinel = object()
    for dict_ in (
        _rc_proplot_default,
        _rc_matplotlib_default,
        _rc_matplotlib_default_full,
    ):
        value = dict_.get(key, sentinel)
        if value is not sentinel:
            return value
    raise KeyError(f'Invalid key {key!r}.')


def _gen_yaml_table(rcdict, comment=True, description=True):
    """
    Return the settings as a nicely tabulated YAML-style table.
    """
    NoneType = type(None)
    prefix = '# ' if comment else ''
    data = []
    for key, pair in rcdict.items():
        # Optionally append description
        if description and isinstance(pair, tuple):  # add commented out description
            value = pair[0]
            descrip = '# ' + pair[1]
        else:
            descrip = ''
            if isinstance(pair, tuple):
                value = pair[1]
            else:
                value = pair

        # Translate object to string
        if isinstance(value, cycler.Cycler):  # special case!
            value = repr(value)
        elif isinstance(value, (str, numbers.Number, NoneType)):
            value = str(value)
        elif isinstance(value, (list, tuple, np.ndarray)) and all(
            isinstance(val, (str, numbers.Number)) for val in value
        ):
            value = ', '.join(str(val) for val in value)
        else:
            warnings._warn_proplot(
                f'Failed to write rc setting {key} = {value!r}. Must be string, '
                'number, or list or tuple thereof, or None or a cycler.'
            )
            continue
        if value[:1] == '#':  # e.g. HEX string
            value = repr(value)
        data.append((key, value, descrip))

    # Generate string
    string = ''
    keylen = len(max(rcdict, key=len))
    vallen = len(max((tup[1] for tup in data), key=len))
    for key, value, descrip in data:
        space1 = ' ' * (keylen - len(key) + 1)
        space2 = ' ' * (vallen - len(value) + 2) if descrip else ''
        string += f'{prefix}{key}:{space1}{value}{space2}{descrip}\n'

    return string.strip()


def _gen_rst_table():
    """
    Return the settings in an RST-style table.
    """
    # Initial stuff
    colspace = 2  # spaces between each column
    descrips = tuple(descrip for _, descrip in _rc_proplot.values())
    keylen = len(max((*_rc_proplot, 'Key'), key=len)) + 4  # for literal backticks
    vallen = len(max((*descrips, 'Description'), key=len))
    divider = '=' * keylen + ' ' * colspace + '=' * vallen + '\n'
    header = 'Key' + ' ' * (keylen - 3 + colspace) + 'Description\n'

    # Build table
    string = divider + header + divider
    for key, (_, descrip) in _rc_proplot.items():
        spaces = ' ' * (keylen - (len(key) + 4) + colspace)
        string += f'``{key}``{spaces}{descrip}\n'

    string = string + divider
    return string.strip()
