<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="recipe">
    <html>
	    <head>
        <title><xsl:value-of select="head/title"/></title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>
        <link rel="stylesheet" href="style.css"></link>
      </head>
      <body>
        <div class="menubar">
          <a href="rezepte.html"><i class="fa fa-fw fa-home"></i></a>
        </div>
        <div class="main">
          <xsl:apply-templates />
        </div>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="title">
    <DIV font-size="20pt" color="black">
      <H1 ALIGN="center"><font color="black"><xsl:apply-templates/></font>
      </H1>
    </DIV>
  </xsl:template>

  <xsl:template match="subtitle">
    <DIV font-size="18pt" color="black">
      <H1 ALIGN="center"><font color="black">aka <xsl:apply-templates/>
      </font></H1>
    </DIV>
  </xsl:template>

  <xsl:template match="categories">
  </xsl:template>

  <xsl:template match="version">
  </xsl:template>

  <xsl:template match="preptime">
	<p>Zubereitungszeit: <xsl:apply-templates /></p>
  </xsl:template>
  
  <xsl:template match="difficulty">
	<p>Schwierigkeitsgrad: <xsl:apply-templates /></p>
  </xsl:template>
  
  <xsl:template match="energy[@type='piece']">
	<p><xsl:apply-templates /> pro Stück</p>
  </xsl:template>
  
  <xsl:template match="energy[@type='person']">
	<p><xsl:apply-templates /> pro Person</p>
  </xsl:template>
  
  <xsl:template match="energy[@type='total']">
	<p><xsl:apply-templates /></p>
  </xsl:template>

  <xsl:template match="yield">
  </xsl:template>

  <xsl:template match="source">
    <p>Adapted from
      <xsl:apply-templates />
    </p>
  </xsl:template>

  <xsl:template match="description">
    <p><xsl:apply-templates />
    </p>
  </xsl:template>

  <xsl:template match="version">
  </xsl:template>

  <xsl:template match="yield">
      Rezept für <xsl:apply-templates/>
  </xsl:template>
  
  <xsl:template match="ingredients">
    <ul>
      <xsl:apply-templates select="ing"/>
      <xsl:apply-templates select="ing-div"/>
    </ul>	
  </xsl:template>

  <xsl:template match="ing-div/title">
      <H2><xsl:apply-templates /></H2>
  </xsl:template>
    
  <xsl:template match="ing">
    <li>
      <xsl:apply-templates />
    </li>
  </xsl:template>

  <xsl:template match="unit">
      <xsl:text> </xsl:text><xsl:apply-templates />
  </xsl:template>
  
  <xsl:template match="energyunit">
      <xsl:text> </xsl:text><xsl:apply-templates />
  </xsl:template>
  
  <xsl:template match="timeunit">
      <xsl:text> </xsl:text><xsl:apply-templates />
  </xsl:template>

  <xsl:template match="item">
      <xsl:text> </xsl:text><xsl:apply-templates />
  </xsl:template>

  <xsl:template match="directions">
    <ol>
      <xsl:apply-templates select="step"/>
    </ol>	
  </xsl:template>

  <xsl:template match="step">
    <li>
      <xsl:apply-templates />
    </li>
  </xsl:template>

  <xsl:template match="sides">
    Beilagen:
    <ul>
    <xsl:apply-templates select="side"/>
    </ul>
  </xsl:template>

  <xsl:template match="side">
    <li>
    <xsl:apply-templates />
    </li>
  </xsl:template>

  <xsl:template match="tags">
    <xsl:apply-templates select="tag"/>
  </xsl:template>

  <xsl:template match="tag">
  </xsl:template>

</xsl:stylesheet>
