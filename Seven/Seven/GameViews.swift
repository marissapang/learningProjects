//
//  GameViews.swift
//  Seven
//
//  Created by apple on 6/12/20.
//  Copyright © 2020 KnowledgeIsBacon. All rights reserved.
//

import UIKit

class TileView: UIView {

    init(x: CGFloat, y: CGFloat){
        super.init(frame: CGRect(x: x, y: y, width: 100, height: 100))
        backgroundColor = UIColor.green
    }
    
    required init?(coder aDecoder: NSCoder){
        super.init(coder: aDecoder)
        //fatalError("NSCoding not supported")
    }

}
